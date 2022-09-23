# -*- coding: utf-8 -*-
# from odoo import http


# class SaleSnakebyte(http.Controller):
#     @http.route('/sale_snakebyte/sale_snakebyte', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_snakebyte/sale_snakebyte/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_snakebyte.listing', {
#             'root': '/sale_snakebyte/sale_snakebyte',
#             'objects': http.request.env['sale_snakebyte.sale_snakebyte'].search([]),
#         })

#     @http.route('/sale_snakebyte/sale_snakebyte/objects/<model("sale_snakebyte.sale_snakebyte"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_snakebyte.object', {
#             'object': obj
#         })
