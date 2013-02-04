class Config(object):
  DEBUG = False
  CSRF_ENABLED = True
  SECRET_KEY = 'dsdkjsjew8u9sdajkqwc'
  SSH_COMMAND = 'command="scp -v -t /scratch/importfs/galaxy/$user_name",no-port-forwarding,no-X11-forwarding'
  SSH_COMMAND_MSG = 'scp <local_file_name> $user_name@cheaha.uabgrid.uab.edu:'

class ProductionConfig(Config):
  SSH_AUTH_KEY_FILE = '/Users/shantanu/auth_keys_prod'

class DevelopmentConfig(Config):
  DEBUG = True
  SSH_AUTH_KEY_FILE = '/Users/shantanu/auth_keys_dev'


