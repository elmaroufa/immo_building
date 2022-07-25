from odoo import api, fields, models, _

class SaleOrderRentalDate(models.Model):
    _inherit = 'sale.order'

    default_start_date = fields.Date(string='Date Debut')
    default_end_date = fields.Date(string='Date de Fin')
