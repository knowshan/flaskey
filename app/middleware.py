# Flask REMOTE_USER http://flask.pocoo.org/snippets/69/
class RemoteUserMiddleware(object):
  def __init__(self, app):
    self.app = app
  def __call__(self, environ, start_response):
    user = environ.pop('HTTP_REMOTE_USER', None)
    environ['HTTP_REMOTE_USER'] = user
    return self.app(environ, start_response)

