# Copyright 2022 Proxima Technologie Cameroon 
# @author SALY ABBO
# Copyright 2021-2022 
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Rental system',
    'version': '12.0.1.0.1',
    'category': 'Sales',
    'license': 'AGPL-3',
    'summary': 'Adds start date and end date on sale order',
    'author': 'SALY ABBO',
    'depends': ['sale'],
    'data': ['views/sale_order.xml',
             'views/product_template.xml',
             'views/special_invoice_move.xml',
             'report/report_invoice.xml',
    
    ],
    'installable': True,
}
