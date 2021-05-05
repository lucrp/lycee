# -*- coding: utf-8 -*-
from datetime import date

from odoo import api, fields, models


class Student(models.Model):
    _name = "iut.student"
    firstname = fields.Char(string='Prénom', required=True)
    lastname = fields.Char(string='Nom', required=True)
    birthdate = fields.Date(string='Date de naissance')
    age = fields.Integer(string='Age', compute="comp_age")
    class_id = fields.Many2one('iut.class', string="Classe")

    @api.depends("birthdate")
    def comp_age(self):
        for rec in self:
            if rec.birthdate:
                calcul_age = date.today() - rec.birthdate
                rec.age = calcul_age.days / 365.25
            else:
                rec.age = 0
