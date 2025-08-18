from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale, Website

class NewWebsiteSale(WebsiteSale):
    # trying to inherit the WebsiteSale class.

    def _shop_lookup_products(self, attrib_set, options, post, search, website):
        fuzzy_search_term, product_count, search_result = super()._shop_lookup_products(attrib_set, options, post, search, website)
        # need to connect the UID to a partner record first
        user = search_result.env.user
        # iterate over list, removing products that shan't be seen
        for product in search_result:
            product.ensure_one()
            # fails if no partner set, or if user/their parent do not match product's user/parent.
            # note: DIDO mentioned that the logic I used could be replaced with the "&" operator between 2 recordsets.
            #       also that the field commercial_partner_id is the useful field when you want company or the user.
            if product.partner_allowed_id.id == False or user.partner_id.commercial_partner_id.id != product.partner_allowed_id.commercial_partner_id.id:
                search_result = search_result - product
                # product_count -= 1
        
        #return None
        return fuzzy_search_term, product_count, search_result
    
    # TODO: simplify this method, look into controller arg auth='user'
    @http.route([
        '/shop',
        '/shop/page/<int:page>',
        '/shop/category/<model("product.public.category"):category>',
        '/shop/category/<model("product.public.category"):category>/page/<int:page>',
    ], type='http', auth="public", website=True, sitemap=WebsiteSale.sitemap_shop)
    def shop(self):
        print('debug')
        if request.env.user._is_public(): #request.session._is_public_user():
            return request.redirect("/web/login")
        return super().shop(self)

    # TODO: add product restriction code