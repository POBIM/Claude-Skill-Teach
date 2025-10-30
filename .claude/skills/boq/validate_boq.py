#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BOQ Validation Script
ตรวจสอบสัดส่วนงบประมาณและแจ้งเตือนหากผิดปกติ
"""

import sys
import io

# Set UTF-8 encoding for Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Best Practices - สัดส่วนที่แนะนำ
BEST_PRACTICES = {
    "งานเตรียมการ": {
        "min": 0.0,
        "max": 5.0,
        "target": 5.0,
        "warning_threshold": 7.0
    },
    "งานโครงสร้าง": {
        "min": 28.0,
        "max": 32.0,
        "target": 30.0,
        "warning_threshold": 35.0
    },
    "งานสถาปัตยกรรม": {
        "min": 38.0,
        "max": 42.0,
        "target": 40.0,
        "warning_threshold": 35.0  # ต่ำกว่านี้ให้เตือน
    },
    "งานระบบไฟฟ้า": {
        "min": 10.0,
        "max": 14.0,
        "target": 12.0,
        "warning_threshold": 16.0
    },
    "งานระบบสุขาภิบาล": {
        "min": 12.0,
        "max": 16.0,
        "target": 13.0,
        "warning_threshold": 18.0
    }
}

def validate_ratios(boq_data):
    """
    ตรวจสอบสัดส่วนงบประมาณ

    Args:
        boq_data: dict ที่มี key เป็นชื่อหมวดงาน และ value เป็นยอดเงิน

    Returns:
        dict ผลการตรวจสอบ
    """
    total = sum(boq_data.values())

    if total == 0:
        return {
            "status": "error",
            "message": "ยอดรวมเป็น 0 ไม่สามารถคำนวณสัดส่วนได้"
        }

    results = {
        "status": "pass",
        "total": total,
        "categories": {},
        "warnings": [],
        "errors": [],
        "recommendations": []
    }

    # ตรวจสอบแต่ละหมวด
    for category, amount in boq_data.items():
        percentage = (amount / total) * 100

        if category not in BEST_PRACTICES:
            results["warnings"].append(f"ไม่พบ best practices สำหรับหมวด '{category}'")
            results["categories"][category] = {
                "amount": amount,
                "percentage": percentage,
                "status": "unknown"
            }
            continue

        bp = BEST_PRACTICES[category]
        status = "pass"
        messages = []

        # ตรวจสอบว่าอยู่ในช่วงที่แนะนำหรือไม่
        if percentage < bp["min"]:
            status = "warning"
            messages.append(f"ต่ำกว่าค่าแนะนำขั้นต่ำ ({bp['min']}%)")
            results["warnings"].append(
                f"⚠ {category}: {percentage:.2f}% (ควรอยู่ที่ {bp['min']}-{bp['max']}%)"
            )
        elif percentage > bp["max"]:
            status = "warning"
            messages.append(f"สูงกว่าค่าแนะนำสูงสุด ({bp['max']}%)")
            results["warnings"].append(
                f"⚠ {category}: {percentage:.2f}% (ควรอยู่ที่ {bp['min']}-{bp['max']}%)"
            )

        # ตรวจสอบ critical threshold
        if category == "งานเตรียมการ" and percentage > bp["warning_threshold"]:
            status = "error"
            messages.append(f"สูงเกินไปมาก! (>{bp['warning_threshold']}%)")
            results["errors"].append(
                f"❌ {category}: {percentage:.2f}% สูงเกินไป! ควรอยู่ที่ ≤{bp['max']}%"
            )
        elif category == "งานโครงสร้าง" and percentage > bp["warning_threshold"]:
            status = "error"
            messages.append(f"สูงเกินไปมาก! (>{bp['warning_threshold']}%)")
            results["errors"].append(
                f"❌ {category}: {percentage:.2f}% สูงเกินไป! ควรลดลงเป็น ~{bp['target']}%"
            )
        elif category == "งานสถาปัตยกรรม" and percentage < bp["warning_threshold"]:
            status = "error"
            messages.append(f"ต่ำเกินไปมาก! (<{bp['warning_threshold']}%)")
            results["errors"].append(
                f"❌ {category}: {percentage:.2f}% ต่ำเกินไป! ควรเพิ่มเป็น ~{bp['target']}%"
            )

        # คำนวณส่วนต่างจาก target
        diff = percentage - bp["target"]

        results["categories"][category] = {
            "amount": amount,
            "percentage": percentage,
            "target": bp["target"],
            "difference": diff,
            "status": status,
            "messages": messages
        }

    # สร้างคำแนะนำ
    if results["errors"]:
        results["status"] = "fail"
        results["recommendations"].append("🔴 พบข้อผิดพลาดร้ายแรง! ควรปรับสัดส่วนก่อนส่งมอบ")
    elif results["warnings"]:
        results["status"] = "warning"
        results["recommendations"].append("🟡 พบข้อควรปรับปรุง ควรตรวจสอบและปรับสัดส่วน")
    else:
        results["recommendations"].append("🟢 สัดส่วนงบประมาณอยู่ในเกณฑ์ที่ดี!")

    return results


def print_validation_report(results):
    """แสดงรายงานผลการตรวจสอบ"""
    print("\n" + "="*80)
    print("รายงานการตรวจสอบสัดส่วนงบประมาณ BOQ")
    print("="*80)

    print(f"\nยอดรวม: {results['total']:,.2f} บาท")
    print("\nสัดส่วนแต่ละหมวด:")
    print("-" * 80)

    for category, data in results["categories"].items():
        status_icon = {
            "pass": "✅",
            "warning": "⚠️",
            "error": "❌",
            "unknown": "❓"
        }.get(data["status"], "")

        target_str = f"(เป้าหมาย {data['target']}%)" if "target" in data else ""
        diff_str = f"[{data['difference']:+.2f}%]" if "difference" in data else ""

        print(f"{status_icon} {category}: {data['percentage']:.2f}% {target_str} {diff_str}")
        print(f"   จำนวนเงิน: {data['amount']:,.2f} บาท")

        if data.get("messages"):
            for msg in data["messages"]:
                print(f"   → {msg}")

    # แสดง errors
    if results["errors"]:
        print("\n" + "="*80)
        print("❌ ข้อผิดพลาดที่พบ:")
        print("-" * 80)
        for error in results["errors"]:
            print(f"  {error}")

    # แสดง warnings
    if results["warnings"]:
        print("\n" + "="*80)
        print("⚠️  ข้อควรระวัง:")
        print("-" * 80)
        for warning in results["warnings"]:
            print(f"  {warning}")

    # แสดงคำแนะนำ
    print("\n" + "="*80)
    print("💡 คำแนะนำ:")
    print("-" * 80)
    for rec in results["recommendations"]:
        print(f"  {rec}")

    # สรุปผล
    print("\n" + "="*80)
    status_text = {
        "pass": "✅ ผ่านการตรวจสอบ",
        "warning": "⚠️  ผ่านแต่มีข้อควรปรับปรุง",
        "fail": "❌ ไม่ผ่านการตรวจสอบ"
    }
    print(f"สถานะ: {status_text.get(results['status'], 'Unknown')}")
    print("="*80 + "\n")


def validate_from_data(boq_data):
    """ตรวจสอบจากข้อมูล dict"""
    results = validate_ratios(boq_data)
    print_validation_report(results)
    return results


if __name__ == '__main__':
    # ตัวอย่างการใช้งาน
    if len(sys.argv) > 1:
        print("ℹ️  Script นี้รองรับการตรวจสอบข้อมูลที่ import เข้ามาเท่านั้น")
        print("ใช้ผ่าน Python module:")
        print("  from validate_boq import validate_from_data")
        print("  validate_from_data(boq_data)")
    else:
        # ตัวอย่างข้อมูลทดสอบ
        print("🧪 ทดสอบด้วยข้อมูลตัวอย่าง:\n")

        # ตัวอย่างที่ 1: BOQ ที่มีปัญหา (ก่อนปรับปรุง)
        print("--- ตัวอย่างที่ 1: BOQ ที่มีปัญหา ---")
        test_data_bad = {
            "งานเตรียมการ": 128000,
            "งานโครงสร้าง": 1577500,
            "งานสถาปัตยกรรม": 1009000,
            "งานระบบไฟฟ้า": 449500,
            "งานระบบสุขาภิบาล": 545000
        }
        validate_from_data(test_data_bad)

        # ตัวอย่างที่ 2: BOQ ที่ถูกต้อง (หลังปรับปรุง)
        print("\n--- ตัวอย่างที่ 2: BOQ ที่ถูกต้องตาม Best Practices ---")
        test_data_good = {
            "งานเตรียมการ": 185450,
            "งานโครงสร้าง": 1112700,
            "งานสถาปัตยกรรม": 1483600,
            "งานระบบไฟฟ้า": 445080,
            "งานระบบสุขาภิบาล": 482170
        }
        validate_from_data(test_data_good)
