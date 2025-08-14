from odoo import fields, models

class PosSession(models.Model):
    _inherit = 'pos.session'

    # original code: https://github.com/odoo/odoo/blob/a456d9c7cbdf17edb5db2c73306b62150e46a7a7/addons/point_of_sale/models/pos_session.py#L2070
    def _loader_params_product_product(self):
        vals = super()._loader_params_product_product()
        vals['context']['display_default_code'] = True
        return vals
