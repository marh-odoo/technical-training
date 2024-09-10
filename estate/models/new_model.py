from odoo import fields, models

class TestModel(models.Model):
    _name = "test.model"
    _description = "Test Model"

    name = fields.Char()
    partner_id = fields.Many2one('res.partner')