# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'My_package',
    'category': 'My_package',
    'summary': 'this package is done by me as beginging oh teklut',
    'description': """
This module gives you a quick view of your contacts directory, accessible from your home page.
You can track your vendors, customers and other contacts.
""",
    'data':[
        'views/cust_menu.xml'
    ],
    'depends': ['base', 'mail'],
    'application': True,
}
