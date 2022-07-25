# -*- coding: utf-8 -*-
from odoo import http

# class ManagerBuilding(http.Controller):
#     @http.route('/manager_building/manager_building/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/manager_building/manager_building/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('manager_building.listing', {
#             'root': '/manager_building/manager_building',
#             'objects': http.request.env['manager_building.manager_building'].search([]),
#         })

#     @http.route('/manager_building/manager_building/objects/<model("manager_building.manager_building"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('manager_building.object', {
#             'object': obj
#         })