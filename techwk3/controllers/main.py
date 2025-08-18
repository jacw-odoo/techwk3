from odoo import fields, models
from odoo.addons.website_sale.controllers.main import WebsiteSale

class NewWebsiteSale(WebsiteSale):
    # trying to inherit the WebsiteSale class.

    def _shop_lookup_products(self, attrib_set, options, post, search, website):
        fuzzy_search_term, product_count, search_result = super()._shop_lookup_products(attrib_set, options, post, search, website)
        # need to connect the UID to a partner record first
        user = search_result.env["res.users"].browse(search_result.env.context["uid"])
        # iterate over list, removing products that shan't be seen
        for product in search_result:
            product.ensure_one()
            if product.partner_allowed_id.id == False or user.partner_id.id != product.partner_allowed_id.id:
                search_result = search_result - product
                product_count -= 1
        
        #return None
        return fuzzy_search_term, product_count, search_result

