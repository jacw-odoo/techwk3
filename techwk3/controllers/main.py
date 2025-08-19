from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale, Website

class NewWebsiteSale(WebsiteSale):
    # trying to inherit the WebsiteSale class.

    def _shop_lookup_products(self, attrib_set, options, post, search, website):
        fuzzy_search_term, product_count, search_result = super()._shop_lookup_products(attrib_set, options, post, search, website)
        user_commercial_id = search_result.env.user.partner_id.commercial_partner_id.id

        for product in search_result:
            product.ensure_one()
            # fails if no partner set, or if user/their parent do not match product's user/parent.
            # note: I had worse logic before (comparing partners and their parents). Dirk reminded
            #       me that the field "commercial_partner_id" is useful here, either parent or self
            if product.partner_allowed_id.id == False or user_commercial_id != product.sudo().partner_allowed_id.commercial_partner_id.id:
                search_result = search_result - product
                product_count -= 1
        
        return fuzzy_search_term, product_count, search_result
    
    # TODO: simplify this method, look into controller arg auth='user', add product
    @http.route([
        '/shop',
        '/shop/page/<int:page>',
        '/shop/category/<model("product.public.category"):category>',
        '/shop/category/<model("product.public.category"):category>/page/<int:page>',
    ], type='http', auth="public", website=True, sitemap=WebsiteSale.sitemap_shop)
    def shop(self):
        if request.env.user._is_public():
            return request.redirect("/web/login")
        return super().shop(self)