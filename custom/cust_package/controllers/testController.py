from odoo import http


class MyController(http.Controller):
    @http.route('/some_url', auth='public')
    def handler(self):
        return 'hre you got tme'


class Extension(MyController):
    @http.route()
    def handler(self):
        do_before()
        return super(Extension, self).handler()


def do_before():
    print('doing before')
