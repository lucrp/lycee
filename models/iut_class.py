# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Class(models.Model):
    _name = "iut.class"
    name = fields.Char('Nom', required=True)
    level = fields.Selection([('1', 'Seconde'), ('2', 'Première'), ('3', 'Terminale')])
    teacher_ids = fields.Many2many("res.partner", string="Professeurs")
    student_ids = fields.One2many("iut.student", "class_id", string="Etudiants")
    student_nb = fields.Integer(string="Nb d'étudiants", compute='comp_students')
    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'Le nom de la classe doit être unique'),
    ]

    @api.depends("student_ids")
    def comp_students(self):
        for rec in self:
            if rec.student_ids:
                rec.student_nb = len(rec.student_ids)
            else:
                rec.student_nb = 0
