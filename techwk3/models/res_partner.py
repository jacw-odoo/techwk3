from odoo import fields, models

class Partner(models.Model):
    _inherit = "res.partner"

    product_allowlist_ids = fields.One2many("product.template", "partner_allowed_id")