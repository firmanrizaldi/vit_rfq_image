# -*- coding: utf-8 -*-
from odoo import http

# class VitRfqImage(http.Controller):
#     @http.route('/vit_rfq_image/vit_rfq_image/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_rfq_image/vit_rfq_image/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_rfq_image.listing', {
#             'root': '/vit_rfq_image/vit_rfq_image',
#             'objects': http.request.env['vit_rfq_image.vit_rfq_image'].search([]),
#         })

#     @http.route('/vit_rfq_image/vit_rfq_image/objects/<model("vit_rfq_image.vit_rfq_image"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_rfq_image.object', {
#             'object': obj
#         })