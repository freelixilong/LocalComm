# -*- coding:utf-8 -*-  
# 
def handle_400(request):
    kwargs = {
        'name': _('Bad Request'),
        'content': _('The request could not be understood by the server.'),
    }
    return handle_error(request, 400, **kwargs)


def handle_403(request):
    kwargs = {
        'name': _('Forbidden'),
        'content': _('You don\'t have permission to access the requested resource.'),
    }
    return handle_error(request, 403, **kwargs)


def handle_404(request):
    kwargs = {
        'name': _('Not Found'),
        'content': _('The requested resource could not be found.'),
    }
    return handle_error(request, 404, **kwargs)


def handle_500(request):
    kwargs = {
        'name': _('Server Error'),
        'content': _('A server error has occurred.'),
    }
    return handle_error(request, 500, **kwargs)