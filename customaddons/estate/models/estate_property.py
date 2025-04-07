from odoo import fields,models
from odoo.api import readonly


class EstateProperty(models.Model):
    _name="estate.property"
    _description = "Descriereeeee"

    name=fields.Char(
        required=True,#this makes the collumn not nullable corresponding to the "name" field in the table estate_property of the database
        default='Unknown',

    )
    description=fields.Text()
    postcode=fields.Char()
    date_availability=fields.Date(
        copy=False,
        default=fields.Date.today(),
    )
    expected_price=fields.Float(required=True,)
    selling_price=fields.Float(readonly=True,copy=False,)
    bedrooms=fields.Integer()
    living_area=fields.Integer()
    facades=fields.Integer()
    garage=fields.Boolean()
    garden=fields.Boolean()
    garden_area=fields.Integer()
    garden_orientation = fields.Selection([
        #   ('','' ), #blank if required=False
            ('north', 'North'),#(how do you reference it in code, how the user sees it in the web browser)
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West'),
        ])
    active=fields.Boolean()
    state=fields.Selection(
        selection=[
    #   ('','' ), #blank if required=False
        ('new','New'),#(how do you reference it in code, how the user sees it in the web browser)
        ('offer_received','Offer received'),
        ('offer_accepted','Offer accepted'),
        ],
        string='State',
        required=True,#if set to False(by default its false) it will create a blank option above all the other options specified in selection attribute
        readonly=False,
        copy=True,
        # tracking=True,
        default='new'

    )