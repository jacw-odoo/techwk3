from odoo import api,fields,models

class Company(models.Model):
    _inherit = "res.company"

    
    def _create_product_group_sequence(self):
        company_ids = self.env["res.company"].search([])
        product_group_vals = []
        for company in company_ids:
            for group in ['print','read','scan']:
                if not self.env["ir.sequence"].search([('code','=','product.product.{group}')]):
                    product_group_vals.append({
                        'name':'Product {group} group',
                        'code':'product.product.'+group,
                        'company_id':company.id,
                        'prefix':group[:2].upper()+'.',
                        'padding':6,
                        'number_next':1,
                        'number_increment':1
                    })
        if product_group_vals:
            self.env["ir.sequence"].create(product_group_vals)