# -*- coding: utf-8 -*-
from odoo import http

# class DebugSales(http.Controller):
#     @http.route('/debug_sales/debug_sales/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/debug_sales/debug_sales/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('debug_sales.listing', {
#             'root': '/debug_sales/debug_sales',
#             'objects': http.request.env['debug_sales.debug_sales'].search([]),
#         })

#     @http.route('/debug_sales/debug_sales/objects/<model("debug_sales.debug_sales"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('debug_sales.object', {
#             'object': obj
#         })