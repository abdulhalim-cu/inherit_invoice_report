# -*- coding: utf-8 -*-
{
    'name': "Cutomize Reports",
    'summary': """Inherit company data and logo in invoice report""",
    'description': """Invoice, Report""",

    'author': "Abdul Halim",
    'website': "https://abdulhalim.pythonanywhere.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'application': True,
    'depends': ['base', 'web'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/external_layout_header.xml',
        'views/report_invoice_document_inherit.xml',
        'views/report_expense_inherit.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
}