from odoo import models, fields, api  # type: ignore

class MiModelo(models.Model):
    _name = "mi.modelo"
    _description = "Mi Modelo"

    name = fields.Char(string="Nombre", required=True)
    description = fields.Text(string="Descripción")
    campo1 = fields.Float(string="Campo 1")
    campo2 = fields.Float(string="Campo 2")
    total = fields.Float(string="Total", compute="_compute_total", store=True)
    activo = fields.Boolean(string="Activo", default=True)
    contacto_ids = fields.Many2many("res.partner", string="Contactos")  # Cambio a Many2many

    @api.depends("campo1", "campo2", "activo")
    def _compute_total(self):
        for record in self:
            record.total = (record.campo1 + record.campo2) if record.activo else 0.0



    


