from odoo import api, fields, models

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    price_difference = fields.Boolean(compute="_compute_price_difference",store=True)

    @api.depends("price_unit")
    def _compute_price_difference(self):
        # assume no difference
        self.price_difference = False
        # get list of orders
        prev_orders_with_prod = self.order_partner_id.sale_order_ids.filtered_domain([
            '&', '&',
                ('id','!=',self.order_id.id),
                ('order_line.product_id','=',self.product_id.id),
                ('state','=','sale')
            ])
        # look through each order
        return True