from odoo import api,fields, models, _
from odoo.exceptions import UserError

class StockMove(models.Model):
    _inherit = "stock.move"

    @api.onchange('quantity')
    def _onchange_quantity(self):
        if self.picking_code == 'incoming' and self.quantity > self.product_uom_qty:
            raise UserError(_("You can't receive more than the ordered quantity. Please, enter a different quantity."))