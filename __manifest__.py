# -*- coding: utf-8 -*-
{
    'name': 'Odoo Training',

    'summary': """Training technique""",

    'description': """ 
        exercise practice odoo
    """,
    'autor': 'Payall',

    'developer': 'Willber R.R',

    'website': 'htps://www.odoo.com',

    'category': 'Training',
    'version': '1.0.1',

    'depends': ['mail', 'hr'],

    'data': [
        'views/menu_view.xml',
        'views/libros_view.xml',
        'security/libreria_security.xml',
        'security/ir.model.access.csv',
        'views/hr_employee_view.xml',

    ],

    'demo': [],
}