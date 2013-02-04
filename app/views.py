from flask import request
from flask import session, g, redirect, url_for, abort, render_template, flash

from . import app
from app.forms import KeyForm
from .main import Key

from string import Template

from functools import wraps

# login_required comes from: http://flask.pocoo.org/docs/patterns/viewdecorators/
def login_required(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if g.user is None:
      return redirect(url_for('index', next=request.url))
    return f(*args, **kwargs)
  return decorated_function


@app.before_request
def _get_user():
  if request.environ.get('REMOTE_USER'):
    g.user = request.environ.get('REMOTE_USER')
  else:
    g.user = None
  g.user = 'Pavgi'


@app.route('/keys')
def index():
  ssh_command_msg = app.config['SSH_COMMAND_MSG']
  user_name = g.user
  return render_template('index.html', title="Home", user_name=user_name, ssh_command_msg=ssh_command_msg)


@app.route('/keys/new', methods=['GET'])
@login_required
def new():
  form = KeyForm()
  user_name = g.user
  d = dict(user_name=user_name)
  ssh_command = Template(app.config['SSH_COMMAND']).substitute(d)
  return render_template('new.html', title='New Key', user=user_name, form=form, ssh_command=ssh_command)


@app.route('/keys/submit', methods=['POST'])
@login_required
def submit():
  value = request.form['ssh_key']
  user_name = g.user
  d = dict(user_name=user_name)
  ssh_command_msg = Template(app.config['SSH_COMMAND_MSG']).substitute(d)
  user_name = g.user
  if Key.valid(value):
    k = Key(value)
    k.submit()
    return render_template('submit.html', ssh_command_msg=ssh_command_msg)
  else:
    flash('Invalid SSH Key. Please submit a new SSH public key.', category='error')
    return redirect(url_for('new'))

  return redirect(url_for('new'))

