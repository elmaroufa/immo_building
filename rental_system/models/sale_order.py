from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    default_start_date = fields.Date(string='Date Debut')
    default_end_date = fields.Date(string='Date de Fin')

    def _prepare_invoice(self):

        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['fac_start_date'] = self.default_start_date
        invoice_vals['fac_end_date'] = self.default_end_date
        return invoice_vals
