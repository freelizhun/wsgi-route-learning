from ps_router import RouterApp

def make_app(mode):
    service_app = RouterApp(mode)
    service_app.add_route("/user/signup", 'UserApp', 'signup')
    service_app.add_route("/user/login", 'UserApp', 'login')
    return service_app


def uwsgi_app():
    mode="debug"
    return make_app(mode)
