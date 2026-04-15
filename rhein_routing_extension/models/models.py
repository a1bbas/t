from odoo import fields, api, models


# ================= MASTER TABLES =================

class Stage(models.Model):
    _name = "stage"
    _description = "Stage"

    name = fields.Char(string="Stage", required=True)

class Color(models.Model):
    _name = "color"
    _description = "Color"

    name = fields.Char(string="Color", required=True)

class Category(models.Model):
    _name = "category"
    _description = "Category"

    name = fields.Char(string="Category", required=True)

class Department(models.Model):
    _name = "department"
    _description = "Department"

    name = fields.Char(string="Department", required=True)

class RoutingType(models.Model):
    _name = "routing.type"
    _description = "Routing Type"

    name = fields.Char(string="Type", required=True)

class Finish(models.Model):
    _name = "finish"
    _description = "Finish"

    name = fields.Char(string="Finish", required=True)


# ================= MRP ROUTING EXTENSION =================

class MrpRouting(models.Model):
    _inherit = "mrp.routing"

    type_id = fields.Many2one("routing.type", string="Type")
    finish_id = fields.Many2one("finish", string="Finish")
    state_id = fields.Many2one("stage", string="Stage")
    color_id = fields.Many2one("color", string="Color")
    category_id = fields.Many2one("category", string="Category")
    department_id = fields.Many2one("department", string="Department")

    additional_info = fields.Char(string="Additional Info")

    route_name = fields.Char(string="Route Name", compute="_compute_route_name", store=True)

    @api.depends(
        "type_id",
        "category_id",
        "department_id",
        "state_id",
        "finish_id",
        "color_id",
        "additional_info",
    )
    def _compute_route_name(self):
        for rec in self:
            parts = [
                rec.type_id.name,
                rec.category_id.name,
                rec.department_id.name,
                rec.state_id.name,
                rec.finish_id.name,
                rec.color_id.name,
                rec.additional_info,
            ]

            rec.route_name = " - ".join(filter(bool, parts))