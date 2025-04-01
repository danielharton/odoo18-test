# -*- coding: utf-8 -*-
from odoo import http


class Danielmodule1(http.Controller):
    @http.route('/danielmodule1/danielmodule1', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/danielmodule1/danielmodule1/objects', auth='public')
    def list(self, **kw):
        return http.request.render('danielmodule1.listing', {
            'root': '/danielmodule1/danielmodule1',
            'objects': http.request.env['danielmodule1.danielmodule1'].search([]),
        })

    @http.route('/danielmodule1/danielmodule1/objects/<model("danielmodule1.danielmodule1"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('danielmodule1.object', {
            'object': obj
        })

