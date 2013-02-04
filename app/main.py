from flask import session, g, redirect, url_for, abort, render_template, flash

import os
from subprocess import call
from tempfile   import NamedTemporaryFile
from contextlib import contextmanager, closing

# imported app to access config[SSH_AUTH_KEY_FILE]
from . import app
print app.config['SSH_AUTH_KEY_FILE']

from string import Template

class Key(object):
  def __init__(self,val):
    self._val = val

  def get_val(self):
    """ Return key's value"""
    return self._val

  def set_val(self, value):
    """ Sets  value """
    self._val = value

  def del_val(self):
    del self._val

  val = property(get_val, set_val, del_val, "SSH key value attribute")

  def submit(self):
    keyfile = app.config['SSH_AUTH_KEY_FILE']
    command_temp = Template(app.config['SSH_COMMAND'])
    d = dict(user_name='ShanTanuPavgi')
    command = command_temp.substitute(d)
    command_key = '%s %s' %(command, self.val)
    with open(keyfile, 'a') as f:
      f.write(command_key + '\n')

  def _find_val_(self,uname):
    """ Find key for given uname """
    with open('/Users/shantanu/.ssh/authorized_keys', 'r') as f:
      l = f.readline
  
  @staticmethod 
  def valid(value):
    with NamedTemporaryFile(delete=False) as fh:
        fh.write(value)
        fh.flush()
        cmd = ('ssh-keygen', '-l', '-f', fh.name)
        ret = call(cmd)
    os.remove(fh.name)

    return ret == 0

