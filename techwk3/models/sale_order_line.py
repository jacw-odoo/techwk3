from odoo import api, fields, models

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    price_difference = fields.Boolean(compute="_compute_price_difference")

    @api.depends("price_unit")
    def _compute_price_difference(self):
        print("price difference")
        # assume no difference
        # get list of orders
        prev_orders_with_prod = self.order_partner_id.sale_order_ids.filtered_domain([
            '&', '&', '&',
                ('id','!=',self.order_id.id),
                ('date_order','<',self.order_id.date_order),
                ('order_line.product_id','=',self.product_id.id),
                ('state','=','sale')
            ])
        # go through results
        if len(prev_orders_with_prod) > 0:
            for line in prev_orders_with_prod[0].order_line.filtered_domain([('product_id','=',self.product_id.id)]):
                # match found, no difference detected
                if line.price_unit == self.price_unit:
                    self.price_difference = False
                    return None
            # no match found, difference detected
            self.price_difference = True
            return None
        # no previous sales order, no difference detected
        self.price_difference = False
        return None
