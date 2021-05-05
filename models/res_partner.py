# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ResPartner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"
    name = fields.Char('Nom', required=True)
    class_ids = fields.Many2many("iut.class", string="Classes")
    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'Le nom de la classe doit être unique')
    ]
