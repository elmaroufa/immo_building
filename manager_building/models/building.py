# -*- coding: utf-8 -*-

from odoo import models, fields, api


#class ResPartner(models.Model):
#    _inherit = 'res.partner'
#
#    mbuilding = fields.Many2one(comodel_name="building_manager", string="batiments")
#    batiment_ids = fields.Many2one(
#        'building_manager', 'manger_bt', string="batiments")
    


class manager_building(models.Model):
    _name = 'building_manager'

    name = fields.Char(string="Nom batiments")
    city = fields.Char(string="Ville")
    district = fields.Char(string="Quartier")
    manager_ids = fields.Selection(
        [('draft', 'SALY ABBO'),
         ('available', 'ABOUBAKAR ABDOULAYE'),
         ('lost', 'OUSMANE NDJIDDA')],
        'Manager', default="draft")
    description = fields.Text(string="Description batiment")




#     @api.depends('value')
#     def _value_pc(self):
#
#     self.value2 = float(self.value) / 100


