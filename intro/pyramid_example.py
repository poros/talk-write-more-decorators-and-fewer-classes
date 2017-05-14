from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config


@view_config(route_name='hello', renderer='string')
def hello_world(request):
    return 'Hello World'


if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello', '/')
    config.scan()
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
