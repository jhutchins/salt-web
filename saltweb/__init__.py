from pyramid.config import Configurator
from pyramid.renderers import JSONP

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_renderer('jsonp', JSONP(param_name='callback'))
    config.add_route('home', '/')
    config.add_route('keys', '/keys/list/{type}/')
    config.scan()
    return config.make_wsgi_app()
