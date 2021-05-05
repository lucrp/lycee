# -*- coding: utf-8 -*-
from datetime import date

from odoo import api, fields, models

class Schedule(models.Model):
    _name = "iut.schedule"
    date_start = fields.Datetime(string="Horaire début")
    date_stop = fields.Datetime(string="Horaire fin")
    room = fields.Char(string="Salle de classe")
    class_id = fields.Many2one('iut.class', string="Classe")
    course_id = fields.Many2one('iut.course', string="Cours")
