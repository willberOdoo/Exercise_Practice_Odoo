from odoo import models, fields, api


# creamos un modelo (tabla de l base de datos) a partir de una clase

class Libros(models.Model):
    _name = 'libros'  # nombre de la tabla que se va a generar,nombre del  modelo
    _inherit = ['mail.thread', 'mail.activity.mixin']

    supervisor_id = fields.Many2one(comodel_name='hr.employee', string='Supervisor')
    name = fields.Char(string="Nombre del libro", required=True,
                       tracking=True)  # nombre del campo tipo cadena
    editorial = fields.Char(strin="Editorial", required=True)
    isbn = fields.Char(string="ISBN", required=True)
    autor_id = fields.Many2one(comodel_name="autor",
                               string="Autor",
                               required=True)  # relacion Many2one conel modelo libros.py
    lastname_autor = fields.Char(related="autor_id.last_name", string="Apellidos del Autor")
    image = fields.Binary(string="Image")
    categoria_id = fields.Many2one(comodel_name="categoria.libro")  # categoria_id  este campo se relaciona con la vista
    literatura_id = fields.Many2one(comodel_name="categoria.libro")
    viaje_id = fields.Many2one(comodel_name="categoria.libro")
    biografia_id = fields.Many2one(comodel_name="categoria.libro")
    monografia_id = fields.Many2one(comodel_name="categoria.libro")
    state = fields.Selection([('draft', 'Borrador'), ('published', 'Publicado')], default='draft')
    description = fields.Char(string="Descripcion", compute="_compute_description")

    # funcion computo
    @api.depends('name')
    def _compute_description(self):
        self.description = self.name + ' | ' + self.isbn + ' | ' + self.autor_id.name + ' | ' + self.categoria_id.name

    # funcion que permite cambiar el estado del libro
    def boton_publicar(self):  # el nombre del boton debe ser el mism que el del campo en la view
        self.state = 'published'

    def boton_borrador(self):
        self.state = 'draft'

    _sql_constraints = [("name_uniq", "unique (name)", "El nombre del libro ya exidste!!")]
    # nombre del sql constraint
    # unique () los valores que no queremos que se dupliquen
    # mensaje de error
    # propiedad que evita que se  dupliqun los registros


class CategoriaLibro(models.Model):
    _name = 'categoria.libro'  # nombre del modelo

    name = fields.Char(string="nombre de la categoria")
