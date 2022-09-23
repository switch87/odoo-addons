# -*- coding: utf-8 -*-

from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_unset_private_sale(self):
        return self.write({'state':'sale'})

    def action_set_to_private_sale(self):
        return self.write({'state':'private_sale'})

    state = fields.Selection(selection_add=[('private_sale','Private Sale')])
