from odoo import api, fields, models, _

class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    fac_start_date = fields.Date(string='Date Debut Location', required=False)
    fac_end_date = fields.Date(string='Date de Fin Location', required=False)
