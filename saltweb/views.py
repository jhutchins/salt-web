from pyramid.view import view_config

import keys

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project':'salt-web'}

@view_config(route_name='keys', renderer='jsonp')
def manage_keys(request):
    func = getattr(keys, 'get_{type}'.format(**request.matchdict))
    return func()
