from odoo import fields, models

class Partner(models.Model):
    _inherit = "res.partner"

    product_allowlist_ids = fields.One2Many("product.template", "partner_allowed")