from odoo import api,fields,models

class ProductTemplate(models.Model):
    _inherit = "product.template"

    product_group = fields.Selection([('print','Printer'),('read','Reader'),('scan','Scanner')],compute="_compute_product_group",inverse="_set_product_group",search="_search_product_group")
    # barcode
    
    @api.depends("product_variant_ids.product_group")
    def _compute_product_group(self):
        self._compute_template_field_from_variant_field('product_group')

    def _search_product_group(self, operator, value):
        subquery = self.with_context(active_test=False)._search([
            ('product_variant_ids.product_group', operator, value),
        ])
        return [('id', 'in', subquery)]

    def _set_product_group(self):
        self._set_product_variant_field('product_group')