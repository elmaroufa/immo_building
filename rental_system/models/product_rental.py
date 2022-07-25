from odoo import api, fields, models, _

class ProductRental(models.Model):
    _inherit = 'product.template'

    rental_ok = fields.Boolean(string="Bien de location",default=False)

   
