from odoo import api,fields,models

class ProductProduct(models.Model):
    _inherit = "product.product"

    product_group = fields.Selection([('pr','Printer'),('re','Reader'),('sc','Scanner')])
    barcode = fields.Char(compute="_compute_barcode", store=True, readonly=False)

    @api.depends("product_group")
    def _compute_barcode(self):
        if self.product_group and self.barcode == False or self.product_group.lower() != self.barcode[:2]:
            self.barcode = self.product_group.upper() + '.' + '{:0>6}'.format((type(self.id) == int and self.id) or self.id.origin)
        else:
            self.barcode = False
        