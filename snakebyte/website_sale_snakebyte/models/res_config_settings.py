# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.tools.translate import _, html_translate

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    out_of_stock_msg = fields.Html('Default Out of Stock Message', related="website_id.out_of_stock_msg" ,readonly=False, translate=html_translate);
