from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    virtual_available_stored = fields.Float(
        string="Virtual Available (Stored Mirror)",
        compute="_compute_virtual_available_stored",
        store=True,
        help="Mirror of virtual_available to enable automated action triggers.",
    )

    @api.depends(
        "product_variant_ids.stock_move_ids.state",
        "product_variant_ids.stock_quant_ids.quantity",
    )
    def _compute_virtual_available_stored(self):
        for template in self:
            template.virtual_available_stored = template.virtual_available
