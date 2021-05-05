# -*- coding: utf-8 -*-
{
    'name': "Lycée",
    'version': '1.0.0',
    'depends': ['base'],
    'author': "Lucas Ramos Paiva",
    'website': "https://github.com/lucrp/lycee/",
    'category': 'Inventory',
    'description': "Ce module sert à gérer les classes, les étudiants et les professeurs d'un Lycée",
    'license': 'LGPL-3',
    # data files always loaded at installation
    'data': [
        'views/res_partner_view.xml',
        'views/iut_student_view.xml',
        'views/iut_class_view.xml',
        'views/iut_schedule_view.xml',
        'lycee_menu.xml',
    ],
    'auto_install': False,
    'installable': True
}
