# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)

class Website(models.Model):
    _inherit = 'website'

    google_tag_manager_id = fields.Char();
