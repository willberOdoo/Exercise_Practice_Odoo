#modelo que le hereda al modulo de empleados propio de Odoo

from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = "hr.employee" #nombre propio de odoo del modelo al que le hare inherit
                             #nombre del modelo que le pasare al view

    is_supervisor = fields.Boolean(string="Es superviosr")#el campo que aparecera en  la vista
