# Flask REMOTE_USER http://flask.pocoo.org/snippets/69/
class RemoteUserMiddleware(object):
  def __init__(self, app):
    self.app = app
  def __call__(self, environ, start_response):
    user = environ.pop('HTTP_X_PROXY_REMOTE_USER', None)
    environ['REMOTE_USER'] = user
    return self.app(environ, start_response)

