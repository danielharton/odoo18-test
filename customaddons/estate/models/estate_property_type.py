# from dateutil.relativedelta import relativedelta

from odoo import fields,models
# from odoo.api import readonly


class EstatePropertyType(models.Model):
    _name="estate.property.type"
    _description = "descriereetip"

    name=fields.Char(required=True)

