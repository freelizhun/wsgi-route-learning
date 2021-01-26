from ps_router import RouterApp

def make_app(mode):
    service_app = RouterApp(mode)
    service_app.add_route("/user/signup", 'UserApp', 'signup')
    service_app.add_route("/user/login", 'UserApp', 'login')
    return service_app

def main():
    import optparse
    parser = optparse.OptionParser(
        usage="%prog [OPTIONS] MODULE:EXPRESSION")
    parser.add_option(
        '-P', '--port', default='8080',
        help='Port to serve on (default 8080)')
    parser.add_option(
        '-H', '--host', default='0.0.0.0',
        help='Host to serve on (default localhost; 0.0.0.0 to make public)')
    parser.add_option(
        '-M', '--mode', default='debug',
        help='debug or prod mode')
    options, args_ = parser.parse_args()

    entry_app = make_app(options.mode)

    if options.mode == 'debug' or 'reset':
        options.port = 8002

    from paste import httpserver
    httpserver.serve(entry_app,host=options.host,port=options.port)

if __name__ == '__main__':
    main()
