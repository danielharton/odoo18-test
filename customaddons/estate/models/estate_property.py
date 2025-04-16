# from dateutil.relativedelta import relativedelta

from odoo import fields,models
# from odoo.api import readonly


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
        default=fields.Date.subtract(fields.Date.today(), months=3),
        # default=fields.Date.today(),
    )
    expected_price=fields.Float(required=True,)
    selling_price=fields.Float(readonly=True,copy=False,)
    bedrooms=fields.Integer(

        default=2,

    )
    living_area=fields.Integer()
    facades=fields.Integer()
    garage=fields.Boolean()
    garden=fields.Boolean()
    garden_area=fields.Integer()
    # integerumeu=fields.Integer()
    # intedfdfsfgerumeu=fields.Integer()
    garden_orientation = fields.Selection([
          # (' ',' ' ), #it puts a blank if required=False
            ('north', 'North'),#(how do you reference it in code, how the user sees it in the web browser)
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West'),

        ],
    # required = True,
        # default=' ',#this also needs to be set if required=True and the ' ' selection exists

    )
    active=fields.Boolean(
        # default=False,#this is the predefined value of the default attribute of the active predefined field
        default=True,#Daca nu am campul active nu o sa am bife la filtre cu include archives,nu o sa pot sa arhivez inregistrari create deja sau pe care le creez in viitor

    )
    state=fields.Selection(
        selection=[#always set db_name=False when changing Selection fields
      # (' ',' ' ), #blank option if required=False
        ('new','New'),#(how do you reference it in code, how the user sees it in the web browser)
        ('offer_received','Offer received'),
        ('offer_accepted','Offer accepted'),
            ('sold','Sold'),
            ('cancelled','Cancelled'),
        ],
        # string='State',
        required=True,#if set to False(by default its false) it will create a blank option above all the other options specified in selection attribute
        readonly=False,
        copy=False,
        # tracking=True,
        default='new',


    )
    property_type_id=fields.Many2one("estate.property.type",string="Type")
    salesperson=fields.Many2one(
        "res.users",
        string="Salesman",
        default=lambda self: self.env.user,
    )
    buyer=fields.Many2one(
        "res.partner",
        copy=False,

    )
    tag_ids=fields.Many2many("estate.property.tag",string="Tags")