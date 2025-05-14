
from odoo import fields,models
from odoo.addons.test_inherit.models import res_partner


class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description = "Descriereeeoferta"

    price=fields.Float()
    status=fields.Selection(
        selection=[
            ('accepted','Accepted'),
            ('refused','Refused'),

        ],
        copy=False,
    )
    partner_id=fields.Many2one("res.partner",required=True)
    property_id=fields.Many2one("estate.property",required=True,ondelete="cascade")  # good practice)
