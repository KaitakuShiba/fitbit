import os

reload = os.getenv('RELOAD')
debug = os.getenv('DEBUG')
bind = '127.0.0.1:5000'
# if want to print stdout: '-'
accesslog = os.getenv('LOG')
errorlog = os.getenv('LOG')
loglevel = os.getenv('LOG_LEVEL')
