if __name__ == '__main__': 
    from chatter import app
    
    from gevent.wsgi import WSGIServer
    from werkzeug.contrib.fixers import ProxyFix
    
    # fixes the X-Real-IP header
    app.wsgi_app = ProxyFix(app.wsgi_app)
    
    http_server = WSGIServer(('127.0.0.1', 5000), app)
    http_server.serve_forever()
