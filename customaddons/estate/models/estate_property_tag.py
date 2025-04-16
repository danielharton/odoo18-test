# from dateutil.relativedelta import relativedelta

from odoo import fields,models
# from odoo.api import readonly


class EstatePropertyTag(models.Model):
    _name="estate.property.tag"
    _description = "Descriereeeetage"

    name=fields.Char(
        required=True,#this makes the collumn not nullable corresponding to the "name" field in the table estate_property of the database

    )