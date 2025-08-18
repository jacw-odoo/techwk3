from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = "product.template"

    partner_allowed_id = fields.Many2one("res.partner")