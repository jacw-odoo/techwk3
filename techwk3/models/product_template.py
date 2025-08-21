from odoo import api,fields,models

class ProductTemplate(models.Model):
    _inherit = "product.template"

    pairs_per_case = fields.Integer(string="Pairs per case",default=0)
    price_per_pair = fields.Float(string="Price per pair",default=0.0, digits="Product Price")

    list_price = fields.Float(compute="_compute_list_price",store=True)

    @api.depends("pairs_per_case","price_per_pair")
    def _compute_list_price(self):
        for prod_temp in self:
            prod_temp.list_price = (prod_temp.pairs_per_case * prod_temp.price_per_pair) or prod_temp.list_price
