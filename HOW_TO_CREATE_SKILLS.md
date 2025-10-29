# คู่มือการสร้าง Skills สำหรับ Claude Code

เอกสารฉบับนี้อธิบายวิธีการสร้าง Agent Skills ที่ถูกต้องตามมาตรฐานของ Anthropic Claude Code

## สารบัญ

1. [ภาพรวม Skills](#ภาพรวม-skills)
2. [โครงสร้างพื้นฐาน](#โครงสร้างพื้นฐาน)
3. [ไฟล์ SKILL.md](#ไฟล์-skillmd)
4. [YAML Frontmatter](#yaml-frontmatter)
5. [การเขียน Description ที่ดี](#การเขียน-description-ที่ดี)
6. [การเขียนเนื้อหา Markdown](#การเขียนเนื้อหา-markdown)
7. [Best Practices](#best-practices)
8. [ตัวอย่าง Skills](#ตัวอย่าง-skills)
9. [การทดสอบ Skill](#การทดสอบ-skill)
10. [Common Mistakes](#common-mistakes)

---

## ภาพรวม Skills

### Skills คืออะไร?

**Agent Skills** คือโฟลเดอร์ที่บรรจุคำแนะนำ (instructions), สคริปต์ และทรัพยากรที่ช่วยให้ Claude ทำงานเฉพาะทางได้ดีขึ้น

### คุณสมบัติสำคัญ

- **Model-Invoked**: Claude เรียกใช้อัตโนมัติเมื่อเหมาะสม (ไม่ต้องเรียกด้วย command)
- **Discoverable**: Claude ค้นหาและโหลด Skills ได้เอง
- **Modular**: แต่ละ Skill ทำงานเฉพาะทาง ไม่ซับซ้อน
- **Reusable**: แชร์และนำกลับมาใช้ใหม่ได้ง่าย

### ประเภท Skills

1. **Project Skills** (`.claude/skills/`) - แชร์กับทีม ใน git repo
2. **Personal Skills** (`~/.claude/skills/`) - ใช้เฉพาะบุคคล
3. **Plugin Skills** - มาพร้อมกับ plugins

---

## โครงสร้างพื้นฐาน

### โครงสร้างโฟลเดอร์

Skill ขั้นต่ำ:
```
my-skill/
  └── SKILL.md          # ไฟล์หลัก (required)
```

Skill ที่สมบูรณ์:
```
my-skill/
  ├── SKILL.md          # ไฟล์หลัก (required)
  ├── LICENSE.txt       # ลิขสิทธิ์ (optional แต่แนะนำ)
  ├── README.md         # เอกสารเพิ่มเติม (optional)
  ├── scripts/          # สคริปต์ช่วยเหลือ (optional)
  │   ├── helper.sh
  │   └── validate.py
  ├── templates/        # เทมเพลต (optional)
  │   └── template.ts
  └── examples/         # ตัวอย่าง (optional)
      └── example1.md
```

### กฎการตั้งชื่อโฟลเดอร์

- **ใช้ hyphen-case**: `my-skill-name` (ห้ามใช้ camelCase, snake_case)
- **ตัวพิมพ์เล็ก**: ห้ามใช้ตัวพิมพ์ใหญ่
- **อักขระ**: Unicode alphanumeric + hyphen เท่านั้น
- **ต้องตรงกับ `name` ใน YAML**: ชื่อโฟลเดอร์ต้องเหมือน `name` ใน frontmatter

✅ ถูกต้อง:
```
test-model/
data-validator/
api-helper/
```

❌ ผิด:
```
TestModel/          # ตัวพิมพ์ใหญ่
test_model/         # underscore
test.model/         # dot
```

---

## ไฟล์ SKILL.md

### โครงสร้างไฟล์

ไฟล์ `SKILL.md` ประกอบด้วย 2 ส่วน:

```markdown
---
# YAML Frontmatter (required)
name: skill-name
description: What it does and when to use
---

# Markdown Content (required)
Your instructions here...
```

### ส่วนประกอบ

1. **YAML Frontmatter** (บรรทัด 1-3):
   - เริ่มด้วย `---`
   - YAML properties
   - ปิดด้วย `---`

2. **Markdown Content** (บรรทัด 5 เป็นต้นไป):
   - คำแนะนำสำหรับ Claude
   - ตัวอย่าง
   - Guidelines
   - Reference files

---

## YAML Frontmatter

### Properties ที่ต้องมี (Required)

#### 1. `name`

**คำอธิบาย**: ชื่อ Skill ในรูปแบบ hyphen-case

**กฎ**:
- ตัวพิมพ์เล็กเท่านั้น
- ใช้ hyphen สำหรับคำหลายคำ
- ต้องตรงกับชื่อโฟลเดอร์
- Unicode alphanumeric + hyphen

**ตัวอย่าง**:
```yaml
name: test-model          # ✅ ถูกต้อง
name: api-helper          # ✅ ถูกต้อง
name: data-validator      # ✅ ถูกต้อง

name: TestModel           # ❌ ตัวพิมพ์ใหญ่
name: test_model          # ❌ underscore
name: test.model          # ❌ dot
```

#### 2. `description`

**คำอธิบาย**: อธิบายว่า Skill ทำอะไร และเมื่อไหร่ Claude ควรใช้

**กฎ**:
- **สั้นและชัดเจน**: 1-3 ประโยค
- **รวม 2 ส่วน**: (1) ทำอะไร + (2) เมื่อไหร่ใช้
- **ใส่ keywords**: คำที่ผู้ใช้จะพูด
- **Specific**: ยิ่งเฉพาะเจาะจงยิ่งดี

**สูตร**:
```
[ทำอะไร]. Use when/for [เมื่อไหร่ใช้] or when [สถานการณ์], [keyword1], [keyword2], [keyword3].
```

**ตัวอย่างดี**:
```yaml
# ✅ ดีมาก - specific, มี keywords, บอกชัดเมื่อไหร่ใช้
description: Create benchmark test models with known analytical solutions for FEM validation. Use when validating the FEM engine, testing new analysis features, or demonstrating accuracy with cantilever beams, simply supported beams, portal frames, or continuous beams.

# ✅ ดี - ครบถ้วน
description: Validate structural models with comprehensive error and warning reporting. Use before running analysis, after model changes, or when troubleshooting analysis errors like singular matrices or missing supports.

# ✅ ดี - มี use cases ชัดเจน
description: Calculate section properties for standard structural shapes including rectangular, circular, I-beams, and hollow sections. Use when defining members, comparing sections, or validating section properties.
```

**ตัวอย่างไม่ดี**:
```yaml
# ❌ คลุมเครือ - ไม่บอกเมื่อไหร่ใช้
description: Helps with tests

# ❌ ไม่มี keywords - Claude หาไม่เจอ
description: A tool for structural analysis

# ❌ ยาวเกินไป - ควรสั้นกระชับ
description: This skill provides comprehensive functionality for creating, managing, and validating structural test cases including but not limited to cantilever beams, simply supported beams, continuous beams, portal frames, trusses, and more complex structural systems with the ability to validate against analytical solutions.
```

### Properties ที่ไม่บังคับ (Optional)

#### 3. `license`

**คำอธิบาย**: ข้อมูลลิขสิทธิ์

**แนะนำ**: ใส่เสมอเพื่อความชัดเจน

**รูปแบบ**:
```yaml
# รูปแบบสั้น
license: MIT

# อ้างอิงไฟล์
license: See LICENSE.txt

# เต็ม
license: Complete terms in LICENSE.txt
```

#### 4. `allowed-tools`

**คำอธิบาย**: รายการ tools ที่ Claude สามารถใช้โดยไม่ต้องขออนุญาต

**ใช้ได้เฉพาะ**: Claude Code

**รูปแบบ**:
```yaml
# เครื่องมือเดียว
allowed-tools: Read

# หลายเครื่องมือ (comma-separated)
allowed-tools: Read, Write, Edit

# หลายเครื่องมือ (YAML list)
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
```

**เครื่องมือที่มี**:
- `Read` - อ่านไฟล์
- `Write` - เขียนไฟล์ใหม่
- `Edit` - แก้ไขไฟล์
- `Bash` - รันคำสั่ง bash
- `Glob` - ค้นหาไฟล์ด้วย pattern
- `Grep` - ค้นหาใน content
- `Task` - สร้าง sub-agent

**ตัวอย่างการใช้**:
```yaml
# Read-only skill (ไม่แก้ไขอะไร)
allowed-tools: Read, Grep, Glob

# Full access (สร้าง/แก้ไข/รันสคริปต์)
allowed-tools: Read, Write, Edit, Bash

# Analysis only (อ่านและวิเคราะห์)
allowed-tools: Read, Glob
```

#### 5. `metadata`

**คำอธิบาย**: ข้อมูลเพิ่มเติมแบบ key-value

**รูปแบบ**:
```yaml
metadata:
  author: Your Name
  version: 1.0.0
  created: 2025-10-17
  tags: structural, analysis, testing
```

**คำแนะนำ**: ใช้ key names ที่ไม่ซ้ำกันง่าย

### ตัวอย่าง Frontmatter สมบูรณ์

```yaml
---
name: test-model
description: Create benchmark test models with known analytical solutions for FEM validation. Use when validating the FEM engine, testing new analysis features, or demonstrating accuracy with cantilever beams, simply supported beams, portal frames, or continuous beams.
license: MIT
allowed-tools: Read, Write, Edit, Bash
metadata:
  author: POBIMOpenStructure Team
  version: 1.0.0
  category: testing
---
```

---

## การเขียน Description ที่ดี

### สูตรสำเร็จ

```
[Action Verb] + [What] + [Context]. Use when [Situation 1], [Situation 2], or when [User Keywords].
```

### องค์ประกอบสำคัญ

1. **ทำอะไร (What)**: บอกชัดเจนว่า Skill ทำอะไร
2. **เมื่อไหร่ (When)**: บอกสถานการณ์ที่ควรใช้
3. **Keywords**: คำที่ผู้ใช้จะพูด/พิมพ์
4. **Use Cases**: ตัวอย่างการใช้งานจริง

### เทคนิคการเขียน

#### 1. เริ่มด้วย Action Verb

✅ ดี:
- Create benchmark tests...
- Validate structural models...
- Calculate section properties...
- Generate analysis reports...
- Export data to CSV...

❌ หลีกเลี่ยง:
- A tool for...
- Helps with...
- Can be used to...
- Provides functionality...

#### 2. ใส่ Keywords ที่ผู้ใช้จะพูด

Think: "ผู้ใช้จะพูดอย่างไร?"

**ตัวอย่าง**:

Skill: `test-model`

ผู้ใช้อาจพูด:
- "Create a cantilever test"
- "Validate FEM with a simple beam"
- "Generate benchmark tests"
- "Test the analysis engine"

Description ควรมี keywords เหล่านี้:
```yaml
description: Create benchmark test models with known analytical solutions for FEM validation. Use when validating the FEM engine, testing new analysis features, or demonstrating accuracy with cantilever beams, simply supported beams, portal frames, or continuous beams.
```

#### 3. ระบุ Use Cases ชัดเจน

ใส่สถานการณ์ที่ควรใช้:

```yaml
# ✅ ดี - มี use cases ชัด
description: Validate structural models with comprehensive error reporting. Use before running analysis, after model changes, or when troubleshooting singular matrix errors.

# ❌ ไม่ดี - ไม่บอกว่าใช้เมื่อไหร่
description: Validates structural models
```

#### 4. เฉพาะเจาะจง (Specific)

ยิ่ง specific ยิ่งดี:

```yaml
# ✅ ดีมาก - specific
description: Calculate section properties for rectangular, circular, I-beam, and hollow sections. Use when defining members or comparing structural sections.

# ❌ คลุมเครือ
description: Calculates properties for sections
```

### เทมเพลตสำหรับ Description

#### Template 1: Task-Based

```yaml
description: [Verb] [what] with [features]. Use when [situation 1], [situation 2], or when [keywords appear].
```

ตัวอย่าง:
```yaml
description: Generate comprehensive analysis reports with tables and charts. Use when documenting results, creating deliverables, or when users request "report", "document", or "summary".
```

#### Template 2: Tool-Based

```yaml
description: [Tool name] for [purpose] using [technology/method]. Use for [use case 1], [use case 2], and when working with [domain keywords].
```

ตัวอย่าง:
```yaml
description: Section property calculator for standard structural shapes using classical mechanics formulas. Use for defining members, comparing sections, and when working with beams, columns, or structural design.
```

#### Template 3: Validation-Based

```yaml
description: Validate [what] against [standard/criteria]. Use before [action], after [change], or when troubleshooting [problem].
```

ตัวอย่าง:
```yaml
description: Validate structural models against FEM requirements and support constraints. Use before running analysis, after model changes, or when troubleshooting singular matrices or convergence errors.
```

### ตัวอย่าง Descriptions ที่ดี

```yaml
# Testing Skill
description: Create benchmark test models with known analytical solutions for FEM validation. Use when validating the FEM engine, testing new analysis features, or demonstrating accuracy with cantilever beams, simply supported beams, portal frames, or continuous beams.

# Validation Skill
description: Validate structural models with comprehensive error and warning reporting. Use before running analysis, after model changes, or when troubleshooting singular matrix errors, missing supports, or invalid properties.

# Calculation Skill
description: Calculate section properties for standard structural shapes including rectangular, circular, I-beams, hollow sections, and T-sections. Use when defining members, comparing sections, or validating section properties.

# Data Export Skill
description: Export analysis results to CSV, JSON, or Markdown formats for use in spreadsheets and documentation. Use when processing results externally, creating reports, or archiving data.

# Hand Verification Skill
description: Verify FEM results against classical structural mechanics formulas and hand calculations. Use to validate analysis accuracy, debug unexpected results, or compare with textbook solutions for simple beams and frames.
```

---

## การเขียนเนื้อหา Markdown

### โครงสร้างที่แนะนำ

```markdown
---
name: skill-name
description: ...
---

# Skill Name

Brief introduction (1-2 sentences)

## Overview / Instructions

Main instructions for Claude

## Features / Capabilities

What the skill can do

## Usage Examples

Concrete examples

## Guidelines / Best Practices

Do's and don'ts

## Technical Details (if needed)

Implementation specifics

## References / Resources (if applicable)

Links to docs, files, or examples
```

### หลักการเขียน

#### 1. เขียนให้ Claude อ่าน (ไม่ใช่ผู้ใช้)

Skill content เป็นคำแนะนำสำหรับ **Claude** ไม่ใช่ documentation สำหรับผู้ใช้

```markdown
# ✅ ดี - สั่ง Claude
You are a structural test case generator. Create standard benchmark problems...

# ❌ ไม่ดี - พูดกับผู้ใช้
This skill helps you create test cases...
```

#### 2. ใช้ Active Voice และ Imperative

```markdown
# ✅ ดี
Create benchmark tests with known solutions.
Validate all properties before running.
Generate TypeScript code ready to run.

# ❌ ไม่ดี
Tests can be created...
Properties should be validated...
Code will be generated...
```

#### 3. ให้ตัวอย่างเฉพาะเจาะจง

```markdown
# ✅ ดี - มีตัวอย่างชัดเจน
### Example: Cantilever Beam Test

**Geometry**:
- Length: 5.0 m
- Fixed at left, free at right

**Expected Results**:
- Deflection: -1.302 mm
- Moment: -50.0 kNm

# ❌ ไม่ดี - คลุมเครือ
Create some test cases for beams
```

#### 4. จัดระเบียบด้วย Sections

ใช้ headings เพื่อแบ่งส่วน:

```markdown
# Main Title (H1) - ใช้ครั้งเดียว

## Major Sections (H2)
Main topics

### Sub-sections (H3)
Details

#### Details (H4)
Fine points
```

#### 5. ใช้ Code Blocks

แสดง code, commands, หรือ output:

````markdown
```typescript
// TypeScript code
const node = addNode({ ... });
```

```bash
# Shell commands
npm run test
```

```json
{
  "config": "value"
}
```
````

#### 6. ใช้ Lists

- **Bullet lists**: สำหรับรายการไม่มีลำดับ
- **Numbered lists**: สำหรับขั้นตอน
- **Checklists**: สำหรับ validation

```markdown
## Features

- Feature 1
- Feature 2
- Feature 3

## Steps

1. First step
2. Second step
3. Third step

## Checklist

- [ ] Item 1
- [ ] Item 2
- [x] Completed item
```

#### 7. ใช้ Tables

สำหรับข้อมูลที่เปรียบเทียบ:

```markdown
| Property | Expected | Actual | Status |
|----------|----------|--------|--------|
| Value 1  | 10.0     | 10.1   | ✅     |
| Value 2  | 20.0     | 19.8   | ✅     |
```

#### 8. ใช้ Callouts (ถ้าจำเป็น)

```markdown
**CRITICAL**: Very important information

**NOTE**: Additional information

**WARNING**: Things to watch out for

**TIP**: Helpful advice
```

### Sections ที่ควรมี

#### 1. Overview / Instructions (Required)

อธิบายว่า Claude ควรทำอย่างไร:

```markdown
## Instructions

You are a [role]. When the user requests [action], perform these steps:

1. [Step 1]
2. [Step 2]
3. [Step 3]

[Additional context or guidelines]
```

#### 2. Examples (Highly Recommended)

ให้ตัวอย่างที่เฉพาะเจาะจง:

```markdown
## Examples

### Example 1: Simple Case

**Input**: User requests "Create a cantilever test"

**Output**:
- Generate model with fixed support
- Apply point load at free end
- Include analytical solution
- Provide validation code

### Example 2: Complex Case

[Another example]
```

#### 3. Guidelines (Recommended)

Do's and Don'ts:

```markdown
## Guidelines

**Do**:
- Use metric units (m, kN, kNm)
- Include analytical solutions
- Provide validation code
- Set reasonable tolerances

**Don't**:
- Use imperial units
- Skip validation
- Create overly complex models
```

#### 4. Technical Details (If Needed)

รายละเอียดทางเทคนิค:

```markdown
## Technical Details

### Formulas

Deflection for cantilever:
```
δ = P×L³ / (3×E×I)
```

### Units

- Forces: kN
- Moments: kNm
- Displacements: m (convert to mm for display)
```

#### 5. References (If Applicable)

อ้างอิงไฟล์หรือเอกสารอื่น:

```markdown
## References

- See `examples/cantilever.ts` for complete example
- Formulas from "Structural Analysis" by Hibbeler
- [Documentation link](https://example.com)
```

### เทมเพลต Markdown สมบูรณ์

```markdown
---
name: my-skill
description: [What it does]. Use when [situations] or when [keywords].
license: MIT
allowed-tools: Read, Write, Edit
---

# Skill Name

Brief 1-2 sentence introduction of what this skill does.

## Instructions

You are a [role]. When the user requests [action], follow these steps:

1. [Step 1 with details]
2. [Step 2 with details]
3. [Step 3 with details]

[Additional context that Claude needs to know]

## Key Features

- **Feature 1**: Description
- **Feature 2**: Description
- **Feature 3**: Description

## Usage Examples

### Example 1: [Common Case]

**Scenario**: User requests "[typical request]"

**Action**:
1. Do X
2. Do Y
3. Do Z

**Expected Output**:
```typescript
// Code example
```

### Example 2: [Another Case]

[Another example]

## Guidelines

### Do's

- ✅ Do this
- ✅ Do that
- ✅ Do another thing

### Don'ts

- ❌ Don't do this
- ❌ Avoid that
- ❌ Never do this other thing

## Technical Details (Optional)

### [Technical Topic 1]

Details...

### [Technical Topic 2]

Details...

## Validation / Testing (If Applicable)

How to verify the results:

1. Check X
2. Verify Y
3. Validate Z

## References (If Applicable)

- [Reference file](./examples/example.md)
- [External link](https://example.com)
```

---

## Best Practices

### 1. Keep Skills Focused

**One Skill = One Purpose**

✅ ดี:
- `test-model` - สร้าง benchmark tests
- `validate-model` - ตรวจสอบ model
- `section-calculator` - คำนวณ section properties

❌ ไม่ดี:
- `structural-tools` - ทำหลายอย่าง (ควรแยก)

### 2. Write for Claude, Not Users

Skill content เป็นคำสั่งสำหรับ Claude:

```markdown
# ✅ ดี - Claude เป็น agent
You are a test generator. Create models with...

# ❌ ไม่ดี - พูดกับผู้ใช้
This tool helps you create models...
```

### 3. Be Specific and Actionable

```markdown
# ✅ ดี - specific
Create a cantilever beam with:
- Length: 5.0 m
- Section: 300×400 mm rectangular
- Load: 10 kN downward at free end

# ❌ คลุมเครือ
Create some beam tests
```

### 4. Include Working Examples

ให้ตัวอย่างที่ run ได้จริง:

```markdown
# ✅ ดี - complete code
```typescript
const node = addNode({
  position: [0, 0, 0],
  support: { ux: true, uy: true, uz: true, rx: true, ry: true, rz: true }
});
```

# ❌ ไม่ดี - incomplete
```typescript
const node = addNode({ ... });
```
```

### 5. Use Progressive Disclosure

เริ่มจากข้อมูลสำคัญ แล้วค่อยลงรายละเอียด:

```markdown
## Instructions

[High-level overview]

### Step 1: [First Step]

[Details for step 1]

### Step 2: [Second Step]

[Details for step 2]

For advanced usage, see [Advanced Topics](#advanced).
```

### 6. Reference Other Files

ใช้ไฟล์อื่นเมื่อจำเป็น:

```markdown
For complete examples, see:
- [Simple example](./examples/simple.md)
- [Advanced example](./examples/advanced.md)
- [Template code](./templates/template.ts)
```

### 7. Test Your Skills

ทดสอบว่า Claude เข้าใจและใช้งานได้:

```markdown
# ทดสอบด้วยคำพูดธรรมดา
"Create a cantilever test"
"Validate my model"
"Calculate beam properties"
```

### 8. Version Control

ใส่ version info ใน metadata:

```yaml
metadata:
  version: 1.0.0
  updated: 2025-10-17
  changelog: Initial release
```

### 9. Document Dependencies

บอกถ้ามี dependencies:

```markdown
## Requirements

- Node.js 18+
- TypeScript 5+
- Dependencies: lodash, moment

## Installation

Install required packages:
```bash
npm install lodash moment
```
```

### 10. Keep Updated

Update Skills เมื่อโค้ดเปลี่ยน:

```markdown
## Version History

### 1.1.0 (2025-10-17)
- Added support for portal frames
- Improved validation logic

### 1.0.0 (2025-10-01)
- Initial release
```

---

## ตัวอย่าง Skills

### Example 1: Simple Skill (Minimal)

**File**: `.claude/skills/hello-world/SKILL.md`

```markdown
---
name: hello-world
description: Generate friendly greeting messages. Use when user requests greetings, welcomes, or hello messages.
---

# Hello World

Generate friendly greeting messages.

## Instructions

When the user requests a greeting, generate a warm and friendly message.

## Examples

**User**: "Say hello"
**Output**: "Hello! How can I help you today?"

**User**: "Welcome message"
**Output**: "Welcome! I'm here to assist you."

## Guidelines

- Keep greetings friendly and professional
- Personalize when possible
- Keep it brief (1-2 sentences)
```

### Example 2: Technical Skill (Complete)

**File**: `.claude/skills/test-model/SKILL.md`

```markdown
---
name: test-model
description: Create benchmark test models with known analytical solutions for FEM validation. Use when validating the FEM engine, testing new analysis features, or demonstrating accuracy with cantilever beams, simply supported beams, portal frames, or continuous beams.
allowed-tools: Read, Write, Edit, Bash
license: MIT
metadata:
  version: 1.0.0
  category: testing
  author: POBIMOpenStructure Team
---

# Test Model Generator

You are a structural test case generator. Create standard benchmark problems used in structural analysis textbooks and FEM validation.

## Available Test Cases

### 1. Cantilever Beam
- Fixed at one end, free at other
- Point load or UDL
- Analytical solution available

### 2. Simply Supported Beam
- Pinned supports at both ends
- Point load at center or UDL
- Known reactions and moments

### 3. Portal Frame
- Fixed base supports
- Horizontal and/or vertical loads
- Frame deformation patterns

## Instructions

When the user requests a test case:

1. **Identify test type**: Determine which test case is needed
2. **Define parameters**: Set geometry, material, loads
3. **Calculate analytical solution**: Use classical formulas
4. **Generate code**: Create TypeScript code to build model
5. **Provide validation**: Include code to check results

## Example: Cantilever Beam

### Problem Definition

**Geometry**:
- Length: 5.0 m
- Fixed at left, free at right

**Material**:
- Steel S355
- E = 200 GPa

**Section**:
- Rectangular 300×400 mm
- I = 1.6e-3 m⁴

**Load**:
- Point load: 10 kN downward at free end

### Analytical Solution

Maximum deflection:
```
δ = P×L³ / (3×E×I)
δ = 10,000 × 5³ / (3 × 200×10⁹ × 1.6×10⁻³)
δ = 0.001302 m = 1.302 mm
```

Maximum moment:
```
M = -P × L = -10 × 5 = -50 kNm
```

### Generated Code

```typescript
import { useAppStore } from '@/store';

const { addNode, addMember } = useAppStore.getState();

// Create fixed support
const fixed = addNode({
  position: [0, 0, 0],
  support: { ux: true, uy: true, uz: true, rx: true, ry: true, rz: true }
});

// Create free end with load
const free = addNode({
  position: [5, 0, 0],
  support: { ux: false, uy: false, uz: true, rx: true, ry: true, rz: false },
  loads: [{
    id: 'load-1',
    loadCaseId: 'dead-load',
    direction: 'global-y',
    magnitude: -10.0
  }]
});

// Create beam
const beam = addMember({
  startNodeId: fixed.id,
  endNodeId: free.id,
  kind: 'beam',
  section: {
    area: 0.12,
    inertiaY: 1.6e-3,
    inertiaZ: 0.9e-3,
    torsionConstant: 0.001,
    depth: 0.4,
    width: 0.3
  }
});
```

### Validation

Expected results:
- Deflection: -1.302 mm (±2%)
- Moment: -50.0 kNm (±1%)
- Reaction: 10.0 kN (±0.5%)

## Guidelines

### Do

- ✅ Use simple geometry (easy to verify)
- ✅ Provide complete analytical solutions
- ✅ Include validation code
- ✅ Set reasonable tolerances (1-2%)
- ✅ Use metric units (m, kN, kNm)

### Don't

- ❌ Create overly complex tests
- ❌ Skip analytical solutions
- ❌ Use unrealistic parameters
- ❌ Mix unit systems

## Test Suite Organization

```markdown
# FEM Validation Test Suite

## Basic Tests
1. ✅ Cantilever with end load
2. ✅ Simply supported beam - point load
3. ⏳ Portal frame

Legend: ✅ Pass | ❌ Fail | ⏳ Not Run
```

## References

- Classical beam formulas: "Structural Analysis" by Hibbeler
- FEM validation: "Finite Element Analysis" by Logan
```

### Example 3: Skill with Scripts

**Structure**:
```
data-validator/
  ├── SKILL.md
  ├── scripts/
  │   ├── validate.py
  │   └── check.sh
  └── templates/
      └── validation_report.md
```

**SKILL.md**:
```markdown
---
name: data-validator
description: Validate data files against schema and rules. Use when checking data integrity, validating imports, or troubleshooting data issues.
allowed-tools: Read, Bash
---

# Data Validator

Validate data files against defined schemas and business rules.

## Instructions

1. Read the data file using Read tool
2. Run validation script: `bash scripts/validate.py <file>`
3. Parse results and report errors
4. Suggest fixes for common issues

## Usage

```bash
# Validate a JSON file
python scripts/validate.py data.json

# Validate with specific schema
python scripts/validate.py data.json --schema custom-schema.json
```

## Validation Rules

- Required fields must be present
- Data types must match schema
- Values must be within valid ranges
- Foreign keys must reference existing records

## Report Format

Use the template in `templates/validation_report.md` to format results.

## Common Issues

### Missing Fields
**Error**: "Required field 'name' not found"
**Fix**: Add the missing field to the data

### Type Mismatch
**Error**: "Expected number, got string"
**Fix**: Convert the value to correct type
```

---

## การทดสอบ Skill

### 1. ทดสอบการค้นหา (Discovery)

ทดสอบว่า Claude หา Skill เจอหรือไม่:

```
# ถาม Claude
"What skills are available?"

# ควรเห็น skill ที่สร้าง
```

### 2. ทดสอบการเรียกใช้ (Activation)

ใช้คำที่มีใน description:

```
# ถ้า description มี "cantilever beams"
"Create a cantilever beam test"

# Claude ควรเรียกใช้ skill อัตโนมัติ
```

### 3. ทดสอบการทำงาน (Functionality)

ดูว่า output ถูกต้อง:

```
# ขอให้สร้าง test
"Create a cantilever test case"

# ตรวจสอบ:
- ✅ Claude เข้าใจคำสั่ง
- ✅ Output ครบถ้วน
- ✅ Code ใช้งานได้
- ✅ มี validation
```

### 4. Debug Checklist

ถ้า Skill ไม่ทำงาน:

```markdown
## Checklist

- [ ] ชื่อโฟลเดอร์ใช้ hyphen-case
- [ ] มีไฟล์ SKILL.md
- [ ] YAML frontmatter ถูกต้อง (--- opening/closing)
- [ ] `name` ตรงกับชื่อโฟลเดอร์
- [ ] `description` มี keywords ที่ผู้ใช้จะพูด
- [ ] `description` บอกว่าเมื่อไหร่ใช้
- [ ] Markdown content ชัดเจน
- [ ] มีตัวอย่าง
- [ ] Restart Claude Code แล้ว
```

### 5. Test Cases

เขียน test cases สำหรับ Skill:

```markdown
## Test Cases

### Test 1: Basic Usage
**Input**: "Create a simple test"
**Expected**: Generate simple test with default parameters

### Test 2: With Parameters
**Input**: "Create a 6m cantilever test"
**Expected**: Generate test with L=6m

### Test 3: Error Handling
**Input**: "Create invalid test"
**Expected**: Show error message and suggest fixes
```

---

## Common Mistakes

### 1. Description ไม่ดี

❌ **Mistake**:
```yaml
description: A tool for testing
```

✅ **Fix**:
```yaml
description: Create benchmark test models with known analytical solutions. Use when validating FEM, testing features, or creating reference problems with cantilever beams, simply supported beams, or portal frames.
```

**ทำไมผิด**: ไม่มี keywords, ไม่บอกเมื่อไหร่ใช้

### 2. ชื่อโฟลเดอร์/name ไม่ตรงกัน

❌ **Mistake**:
```
Folder: test-model/
YAML: name: testModel
```

✅ **Fix**:
```
Folder: test-model/
YAML: name: test-model
```

**ทำไมผิด**: ต้องตรงกันทุกประการ

### 3. YAML Syntax ผิด

❌ **Mistake**:
```yaml
---
name: test-model
description: Create tests...
# ไม่มี closing ---
# Markdown content
```

✅ **Fix**:
```yaml
---
name: test-model
description: Create tests...
---

# Markdown content
```

**ทำไมผิด**: ต้องมี `---` ทั้งเปิดและปิด

### 4. เขียนให้ผู้ใช้อ่าน แทนที่จะเป็น Claude

❌ **Mistake**:
```markdown
This skill helps you create tests for your models.
```

✅ **Fix**:
```markdown
You are a test generator. Create benchmark tests with analytical solutions.
```

**ทำไมผิด**: Skill content เป็นคำสั่งสำหรับ Claude ไม่ใช่ documentation

### 5. Skill ทำหลายอย่าง

❌ **Mistake**:
```
structural-tools/  # ทำหลายอย่าง
  - Create tests
  - Validate models
  - Calculate sections
  - Generate reports
```

✅ **Fix**:
```
test-model/         # เฉพาะ test
validate-model/     # เฉพาะ validation
section-calculator/ # เฉพาะ calculation
report-generator/   # เฉพาะ report
```

**ทำไมผิด**: แต่ละ Skill ควรทำอย่างเดียว

### 6. ไม่มีตัวอย่าง

❌ **Mistake**:
```markdown
Create test models for validation.
```

✅ **Fix**:
```markdown
Create test models for validation.

## Example

```typescript
const node = addNode({
  position: [0, 0, 0],
  support: { ux: true, uy: true, ... }
});
```
```

**ทำไมผิด**: ตัวอย่างช่วยให้ Claude เข้าใจดีขึ้น

### 7. Description ยาวเกินไป

❌ **Mistake**:
```yaml
description: This comprehensive skill provides extensive functionality for creating, managing, validating, and documenting structural test cases including but not limited to cantilever beams, simply supported beams, continuous beams, portal frames, trusses, and various other structural systems with the complete ability to validate results against known analytical solutions derived from classical structural mechanics theory and textbook examples ensuring accuracy and reliability of the finite element analysis engine.
```

✅ **Fix**:
```yaml
description: Create benchmark test models with known analytical solutions for FEM validation. Use when validating the FEM engine, testing features, or creating tests for cantilever beams, simply supported beams, portal frames, or trusses.
```

**ทำไมผิด**: ควรสั้น กระชับ ชัดเจน

### 8. Missing Keywords

❌ **Mistake**:
```yaml
description: Generate tests for analysis validation.
```

✅ **Fix**:
```yaml
description: Generate benchmark tests for FEM validation. Use when validating analysis, testing accuracy, or creating cantilever, beam, or frame tests.
```

**ทำไมผิด**: ต้องมีคำที่ผู้ใช้จะพูด (cantilever, beam, frame)

### 9. ไม่ระบุ Use Cases

❌ **Mistake**:
```yaml
description: Validates models.
```

✅ **Fix**:
```yaml
description: Validates models with error reporting. Use before running analysis, after model changes, or when troubleshooting errors.
```

**ทำไมผิด**: ต้องบอกว่าใช้เมื่อไหร่

### 10. Code Examples ไม่สมบูรณ์

❌ **Mistake**:
```typescript
const node = addNode({ ... });
const member = addMember({ ... });
```

✅ **Fix**:
```typescript
const node = addNode({
  position: [0, 0, 0],
  support: {
    ux: true,
    uy: true,
    uz: true,
    rx: true,
    ry: true,
    rz: true
  }
});

const member = addMember({
  startNodeId: node.id,
  endNodeId: otherNode.id,
  kind: 'beam',
  material: steelS355,
  section: { area: 0.1, inertiaY: 0.001, ... }
});
```

**ทำไมผิด**: ตัวอย่างควร run ได้จริง

---

## สรุป

### Checklist สำหรับสร้าง Skill

```markdown
## Pre-Creation

- [ ] คิดชื่อ Skill (hyphen-case)
- [ ] กำหนด purpose ที่ชัดเจน (one skill, one purpose)
- [ ] เขียน description ที่มี keywords และ use cases
- [ ] เตรียมตัวอย่างที่ชัดเจน

## Structure

- [ ] สร้างโฟลเดอร์ (hyphen-case)
- [ ] สร้างไฟล์ SKILL.md
- [ ] YAML frontmatter ถูกต้อง
- [ ] name ตรงกับชื่อโฟลเดอร์
- [ ] description สมบูรณ์

## Content

- [ ] Instructions ชัดเจน
- [ ] มีตัวอย่างเฉพาะเจาะจง
- [ ] มี guidelines/best practices
- [ ] Code examples สมบูรณ์
- [ ] Reference ไฟล์อื่น (ถ้ามี)

## Testing

- [ ] Claude หา Skill เจอ
- [ ] Claude เรียกใช้เมื่อควรใช้
- [ ] Output ถูกต้อง
- [ ] ทดสอบหลาย scenarios

## Documentation

- [ ] README.md อัพเดท
- [ ] มี LICENSE (ถ้าแชร์)
- [ ] Version info (ถ้าจำเป็น)
```

### Quick Reference

**Minimum Skill**:
```
my-skill/
  └── SKILL.md (with frontmatter + markdown)
```

**Frontmatter Template**:
```yaml
---
name: skill-name
description: [What it does]. Use when [situations] or [keywords].
---
```

**Description Formula**:
```
[Verb] [what] [context]. Use when [situation], [situation], or when [keywords].
```

**Testing**:
```
"[Use keyword from description]" → Should activate skill
```

---

## ทรัพยากรเพิ่มเติม

### Official Documentation

- [Agent Skills Overview](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
- [Skills Best Practices](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices)
- [Skills Quickstart](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/quickstart)

### Examples

- Official Anthropic Skills: `d:\Git\POBIMStructural\skills\`
- Project Skills: `.claude/skills/`

### Templates

- Agent Skills Spec: `skills/agent_skills_spec.md`
- Example Skills: `skills/algorithmic-art/`, `skills/artifacts-builder/`

---

**เอกสารนี้สร้างโดย**: POBIMOpenStructure Development Team
**วันที่อัพเดท**: 2025-10-17
**เวอร์ชัน**: 1.0.0
