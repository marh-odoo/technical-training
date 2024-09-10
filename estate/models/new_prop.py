from odoo import fields, models

class TestModel(models.Model):
    _name = "test.property"
    _description = "Test Model"

    name = fields.Char()
    date = fields.Text()
    name = fields.Char()

    partner_id = fields.Many2one('res.partner')