# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Course(models.Model):
    _name = "iut.course"
    name = fields.Char(string="Nom cours")
