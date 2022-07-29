# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models
from odoo.tools.translate import html_translate

_logger = logging.getLogger(__name__)

class Website(models.Model):
    _inherit = 'website'

    out_of_stock_msg = fields.Html(translate=html_translate);
