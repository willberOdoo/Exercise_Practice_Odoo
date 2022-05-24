from odoo import models, fields, api


# creamos un modelo (tabla de l base de datos) a partir de una clase

class Autor(models.Model):
    _name = 'autor'  # nombre de la tabla que se va a generar

    name = fields.Char(string="Nombre")
    last_name = fields.Char(string="Apellidos")

