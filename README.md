## Version
- Python 3.8.7
- Flask 1.1.2
- gunicorn 20.0.4

## Overview
```bash
$ pip install pipenv
$ cd this_project
$ pipenv --python 3.8
# install package
$ pipenv install -r ./requirements/dev.txt

# run with gunicorn(not requres flusk run)
$ RELOAD=True DEBUG=True LOG='-' LOG_LEVEL='info' SLACK_BOT_TOKEN=$SLACK_BOT_TOKEN SLACK_CHANNEL=$SLACK_CHANNEL FLASK_ENV=development pipenv run gunicorn app:app -c ${PWD}/config/gunicorn_settings.py

$ curl http://localhost:5000
> something response
# version
$ pipenv run python --version
# prod
$ export SLACK_BOT_TOKEN=xoxb-xxxx
$ export SLACK_CHANNEL=xxx #ex: #random
$ pipenv install -r ./requirements/prod.txt
$ RELOAD=False DEBUG=None LOG=None LOG_LEVEL='warning' SLACK_BOT_TOKEN=$SLACK_BOT_TOKEN SLACK_CHANNEL=$SLACK_CHANNEL FLASK_ENV=prodcution pipenv run gunicorn app:app -c ${PWD}/config/gunicorn_settings.py -D
```

## Testing
```bash
# testing
$ pipenv run pytest

# Use Env
$ export SLACK_BOT_TOKEN=xoxb-xxxx
$ export SLACK_CHANNEL=xxx #ex: #random
$ SLACK_BOT_TOKEN=$SLACK_BOT_TOKEN SLACK_CHANNEL=app $SLACK_CHANNEL pipenv run pytest tests/test_check_distance.py
```

## Debug
```python
import pdb

def test():
  pdb.set_trace()
  print('test')

test()
```

## Create DB
```bash
$ pipenv run python migrate.py
```

## AP
```bash
# run Nginx
$ nginx -c ${PWD}/config/nginx.conf
# storp Nginx
$ nginx -s stop

# run gunicorn
$ SLACK_BOT_TOKEN=$SLACK_BOT_TOKEN SLACK_CHANNEL=$SLACK_CHANNEL FLASK_ENV=prodcution pipenv run gunicorn app:app -c ${PWD}/config/gunicorn_settings.py --no-debugger 
# kill gunicorn
$ pkill gunicorn
```

## Ref
- https://towardsdatascience.com/collect-your-own-fitbit-data-with-python-ff145fa10873
- https://python-fitbit.readthedocs.io/en/latest/
- https://tech.gunosy.io/entry/fitbit-activity-notifier#Fitbitのデータを取得するためのトークンを発行する
- https://medium.com/faun/deploy-flask-app-with-nginx-using-gunicorn-7fda4f50066a
- https://qiita.com/mintak21/items/eeba4654a0db21abcb1c
