from odoo import models

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def button_confirm(self):
        result = super().button_confirm()
        for order in self:
            for line in order.order_line:
                # check for product variant first
                vendor_pricelist = self.env["product.supplierinfo"].search([
                    '&',
                        ('product_id','=',line.product_id.id),
                        ('partner_id','=',order.partner_id.id)])
                # then check for a template
                if not vendor_pricelist:
                    vendor_pricelist = self.env["product.supplierinfo"].search([
                        '&','&',
                            ('product_tmpl_id','=',line.product_id.product_tmpl_id.id),
                            ('product_id','=',False),
                            ('partner_id','=',order.partner_id.id)])
                if vendor_pricelist:
                    vendor_pricelist.price = line.price_unit
        return result

