# -*- coding: utf-8 -*-
{
    'name': "Lycée",
    'version': '1.0.0',
    'depends': ['base'],
    'author': "Lucas Ramos Paiva",
    'website': "https://github.com/lucrp/lycee/",
    'category': 'Inventory',
    'description': "Ce module sert à gérer les classes, les étudiants et les professeurs d'un Lycée",
    'license': 'MIT',
    # data files always loaded at installation
    'data': [
        'views/res_partner_view.xml',
        #'lycee_menu.xml',
    ],
    'auto_install': False,
    'installable': True
}
