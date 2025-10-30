# BOQ Skill - README

## โครงสร้าง Folder

```
.claude/skills/boq/
├── boq_helper.py           # Core script สำหรับสร้างและจัดการ BOQ
├── validate_boq.py         # Validation script ตรวจสอบสัดส่วนงบประมาณ
├── recalc.py              # Formula recalculation script
├── BEST_PRACTICES.md      # คู่มือแนวทางการจัดทำ BOQ
├── skill.md               # Skill documentation
├── examples/              # ตัวอย่างการใช้งาน
│   ├── create_house_boq.py
│   └── README.md
└── README.md             # ไฟล์นี้

workspace/boq_examples/    # Output folder สำหรับไฟล์ BOQ ที่สร้าง
└── BOQ_*.xlsx
```

## การใช้งาน

### Quick Start

```bash
# สร้าง BOQ บ้านพักอาศัย 2 ชั้น (ตาม Best Practices)
cd .claude/skills/boq
python examples/create_house_boq.py
```

ไฟล์ BOQ จะถูกสร้างที่: `workspace/boq_examples/BOQ_House_2Story_4M_[timestamp].xlsx`

### สร้าง BOQ แบบกำหนดเอง

```bash
python boq_helper.py create output.xlsx "ชื่อโครงการ" "สถานที่" "ลูกค้า"
```

### ตรวจสอบสัดส่วนงบประมาณ

```python
from validate_boq import validate_from_data

boq_totals = {
    "งานเตรียมการ": 186916,
    "งานโครงสร้าง": 1122092,
    "งานสถาปัตยกรรม": 1495327,
    "งานระบบไฟฟ้า": 448598,
    "งานระบบสุขาภิบาล": 485981
}

validate_from_data(boq_totals)
```

## Best Practices

สัดส่วนงบประมาณมาตรฐาน (สำหรับบ้านพักอาศัย):
- **งานเตรียมการ:** ≤ 5%
- **งานโครงสร้าง:** 28-32% (เป้าหมาย 30%)
- **งานสถาปัตยกรรม:** 38-42% (เป้าหมาย 40%)
- **งานระบบไฟฟ้า:** 10-14% (เป้าหมาย 12%)
- **งานระบบสุขาภิบาล:** 12-16% (เป้าหมาย 13%)

อ่านรายละเอียดเพิ่มเติมใน `BEST_PRACTICES.md`

## Files Description

### Core Scripts
- **`boq_helper.py`** - สร้างและจัดการ BOQ (create, add items)
- **`validate_boq.py`** - ตรวจสอบสัดส่วนงบประมาณ
- **`recalc.py`** - คำนวณ formula ใน Excel

### Documentation
- **`BEST_PRACTICES.md`** - แนวทางการจัดทำ BOQ ที่ถูกต้อง
- **`skill.md`** - Skill documentation (API reference)
- **`README.md`** - ไฟล์นี้

### Examples
- **`examples/create_house_boq.py`** - ตัวอย่างสร้าง BOQ บ้าน 2 ชั้น
- **`examples/README.md`** - คำอธิบายตัวอย่าง

## หมายเหตุสำคัญ

1. **Output Location**: ไฟล์ BOQ จะถูกสร้างที่ `workspace/boq_examples/` เสมอ เพื่อแยกออกจาก skill folder
2. **Best Practices**: ควรตรวจสอบสัดส่วนด้วย `validate_boq.py` ก่อนส่งมอบทุกครั้ง
3. **Formula**: ใช้ Excel formula เสมอ อย่าคำนวณใน Python
4. **Thai Language**: Skill นี้รองรับภาษาไทยเต็มรูปแบบ

## ตัวอย่าง BOQ ที่ได้

BOQ ที่สร้างจะมี:
- ข้อมูลโครงการ (ชื่อ, สถานที่, ลูกค้า)
- 5 หมวดงานมาตรฐาน
- Formula อัตโนมัติ (ราคารวมวัสดุ, ค่าแรงรวม, รวมราคา)
- รวมทั้งโครงการ (ก่อนและหลัง VAT 7%)
- Format สวยงาม มีสี มี border

## การพัฒนาต่อ

หากต้องการเพิ่มตัวอย่างใหม่:
1. สร้างไฟล์ใน `examples/`
2. ตั้งค่า output path ให้ชี้ไปที่ `workspace/boq_examples/`
3. เพิ่มคำอธิบายใน `examples/README.md`

---

*Last updated: 2025-10-29*
