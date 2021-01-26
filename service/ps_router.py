#!/usr/bin/env python
from webob import Request, Response
from webob import exc

from routes import Mapper
from ps_middleware import middleware_factory

class RouterApp:
    """ Route request to the matching wsgiapp. """
    def __init__(self,mode):
        self.map = Mapper()
        self.__routing_table = {} # Maps path to app.
        self.mode = mode

    def __call__(self, environ, start_response):
        req = Request(environ)
        match = self.map.match(req.path_qs)
        if match:
            m = match['middleware']
            handler_string = match['handler'] #类UserApp中的'login'或者'signup'
            class_UserAapp = self.__routing_table[m]
            if class_UserAapp is not None:
                start_response('200 OK', [('Content-Type', 'text/html')])
                #通过getattr方法来获取类UserApp中的login或者siginup方法
                bound_method=getattr(class_UserAapp,handler_string,'None')
                result=bound_method()
                body = '<h1>Hello, %s!</h1>' % (result or 'web')
                return [body.encode('utf-8')]

    def add_route(self, pat, mid, han):
        if mid not in self.__routing_table: # middleware being SINGELTON
            self.__routing_table[mid] = middleware_factory(mid,self.mode)
        self.map.connect(pat,middleware=mid,handler=han)
