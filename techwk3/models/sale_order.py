from odoo import api,fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def _cron_cancel_expired(self, job_count=20):
        """ Cancel quotes with a past expiration date.
        :param job_count: maximum number of jobs to process if specified.
        """
        to_process = self.env["sale.order"].search(
            ['&',('state','=','draft'),('is_expired','=',True)],
            limit=job_count+1)
        
        need_retrigger = len(to_process) > job_count

        for order in to_process[:job_count]:
            order._action_cancel()

        if need_retrigger:
            self.env.ref('techwk3.ir_cron_cancel_expired_quotations')._trigger()
