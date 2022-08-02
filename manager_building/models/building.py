# -*- coding: utf-8 -*-

from odoo import models, fields, api



class ProductBuild(models.Model):
    _inherit = 'product.template'

    building_ids = fields.Many2one("building_manager",string="Batiments", required=False)

   

class ResPartner(models.Model):
    _inherit = 'res.users'

    building_manage = fields.One2many("building_manager", "manager_ids",string="batiments",
    required=False)
   
    


class manager_building(models.Model):
    _name = 'building_manager'

    name = fields.Char(string="Nom batiments")
    city = fields.Char(string="Ville")
    district = fields.Char(string="Quartier")
    manager_ids = fields.Many2one("res.users", string="Manager", required=False)
    product_build = fields.One2many("product.template", "building_ids", string="Produit de location",
    required=False)
    description = fields.Text(string="Description batiment")




#     @api.depends('value')
#     def _value_pc(self):
#
#     self.value2 = float(self.value) / 100


