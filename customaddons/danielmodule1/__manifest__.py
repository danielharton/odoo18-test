# -*- coding: utf-8 -*-
{
    'name': "To-Do List", # div name shortdesc

    'summary': "Summaryul este ", # div name summary

    'description': """
Descrierea care apare sub orice tab: Information,Technical Data, Installed Features etc
    """,

    'author': "Daniel SRL", # div name author
    'website': "https://www.dani.com", #div name website

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Startups Category',# div name category_id
    'version': '1.19',
    # it will show up on page like this: Latest version 18.0.{version}

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

