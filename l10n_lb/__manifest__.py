# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Main contributor: Wafi Chaar frm BAS
# Copyright (C) 2020 BAS (<http://www.bas.sarl>) 

{
    'name': "Lebanon - Accounting",
    'version': '13.3',
    'author': 'BAS',
    'website': 'http://bas.sarl',
    'category': 'Localization',
    'license': 'AGPL-3',	
    'description': """
Lebanon - Accounting localization: 
chart of accounts, tax and stock valuation
by BAS
==========================================
    """,

    'depends': ['account'],

    'data': [
        'data/account_data.xml',
        'data/l10n_lb_chart_data.xml',
        'data/account.account.template.csv',
        'data/l10n_lb_chart_post_data.xml',
        'data/tax_report_data.xml',
        'data/account_tax_template_data.xml',
        'data/account_chart_template_data.xml',
    ],

}
