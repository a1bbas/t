# -*- coding: utf-8 -*-
from email.policy import default

from odoo import models, fields
import logging

from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class reusable_products(models.TransientModel):
    _name = 'reusable_products.reusable_products'

    product_category_id = fields.Many2one('product.category', string="Category")


    def action_create_reusable_products(self):
        active_ids = self.env.context.get('active_ids', [])

        if not active_ids:
            raise ValidationError("No products selected")

        products = self.env['product.template'].browse(active_ids)

        for product in products:
            self.env['product.template'].create({
                'name': product.name + ' - Reusable',
                'categ_id': self.product_category_id.id,
                'default_code': product.default_code + 'R',
                'type': product.type,
                'list_price': product.list_price,
                'image_1920': product.image_1920,
            })

        # self.hide_reusable_comp = True

        return {'type': 'ir.actions.act_window_close'}

    def action_create_sterile_products(self):
        active_ids = self.env.context.get('active_ids', [])

        if not active_ids:
            raise ValidationError("No products selected")

        products = self.env['product.template'].browse(active_ids)

        for product in products:
            self.env['product.template'].create({
                'name': product.name + ' - Sterile',
                'categ_id': self.product_category_id.id,
                'default_code': product.default_code + 'S',
                'type': product.type,
                'list_price': product.list_price,
                'image_1920': product.image_1920,
            })

        return {'type': 'ir.actions.act_window_close'}

