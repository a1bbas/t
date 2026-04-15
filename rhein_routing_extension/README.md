# MRP Routing Customization

## 📌 Overview
This module extends the default **MRP Routing** functionality in Odoo by introducing additional classification fields and a dynamically computed route name.

It helps organize and categorize routing records based on multiple attributes like type, category, department, stage, finish, and color.

---

## 🚀 Features

### ✅ Master Data Models
The following master tables are added:

- Stage
- Color
- Category
- Department
- Routing Type
- Finish

Each model contains:
- `name` (required field)

---

### ✅ MRP Routing Enhancements

The `mrp.routing` model is extended with the following fields:

| Field Name        | Type        | Description |
|------------------|------------|------------|
| type_id          | Many2one   | Routing Type |
| finish_id        | Many2one   | Finish |
| state_id         | Many2one   | Stage |
| color_id         | Many2one   | Color |
| category_id      | Many2one   | Category |
| department_id    | Many2one   | Department |
| additional_info  | Char       | Extra information |

---

### ✅ Computed Field

#### `route_name`
- Type: Char
- Computed and Stored
- Automatically generated based on selected fields

**Logic:**