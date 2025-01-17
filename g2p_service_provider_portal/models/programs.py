# Part of OpenG2P. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class G2PReimbursementProgram(models.Model):
    _inherit = "g2p.program"

    file_size_spp = fields.Float()

    def update_form_template(self):
        if self.is_reimbursement_program:
            form_view = self.self_service_portal_form.view_id
            form_view_template = form_view.arch_db
            form_view.write(
                {
                    "arch_db": form_view_template.replace(
                        "website.layout",
                        "g2p_service_provider_portal.reimbursement_submission_form_template",
                    ).replace(
                        "g2p_self_service_portal.self_service_form_template",
                        "g2p_service_provider_portal.reimbursement_submission_form_template",
                    )
                }
            )
        else:
            return super(G2PReimbursementProgram, self).update_form_template()
