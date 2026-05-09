# -*- coding: utf-8 -*-
{
    'name': "rhein_routing_extension",

    'summary': """
       This Custom module add some new fields in mrp.routing.
       """,
    'author': "Nasir Rhein",
    'category': 'mrp',
    'version': '13.0.0.1',
    'depends': ['base', 'mrp'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_routing_info.xml',
        'views/actions_product_routing_info.xml',
        'views/views.xml',
    ],
}
