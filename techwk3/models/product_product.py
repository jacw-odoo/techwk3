from odoo import api,fields,models

class ProductProduct(models.Model):
    _inherit = "product.product"

    product_group = fields.Selection([('print','Printer'),('read','Reader'),('scan','Scanner')])
    barcode = fields.Char(compute="_compute_barcode", store=True, readonly=False)

    @api.depends("product_group")
    def _compute_barcode(self):
        for product in self:
            if not product.barcode or (product.product_group and
                    product.product_group[:2].upper() != product.barcode[:2]):
                product.barcode = product.env["ir.sequence"].next_by_code(f'product.product.{product.product_group}')
            else:
                product.barcode = False