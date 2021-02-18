import os

reload = os.getenv('RELOAD')
debug = os.getenv('DEBUG')
bind = '127.0.0.1:5000'
# if want to print stdout: '-'
accesslog = os.getenv('ACCESS_LOG')
errorlog = os.getenv('ERROR_LOG')
loglevel = os.getenv('LOG_LEVEL')
