from odoo import api,fields,models

class ProductProduct(models.Model):
    _inherit = "product.product"

    product_group = fields.Selection([('pr','Printer'),('re','Reader'),('sc','Scanner')])
    # barcode
    