## Version
- Python 3.8.7
- Flask 1.1.2

## Overview
```bash
$ pip install pipenv
$ cd this_project
$ pipenv --python 3.8
# install package
$ pipenv install -r ./requirements/dev.txt
# run dev env server
$ SLACK_BOT_TOKEN=$SLACK_BOT_TOKEN SLACK_CHANNEL=$SLACK_CHANNEL FLASK_ENV=development pipenv run flask run
$ curl http://localhost:5000
> something response
# version
$ pipenv run python --version
# prod

$ export SLACK_BOT_TOKEN=xoxb-xxxx
$ export SLACK_CHANNEL=xxx #ex: #random
$ pipenv install -r ./requirements/prod.txt
$ SLACK_BOT_TOKEN=$SLACK_BOT_TOKEN SLACK_CHANNEL=$SLACK_CHANNEL FLASK_ENV=prodcution pipenv run flask run
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

## Ref
- https://towardsdatascience.com/collect-your-own-fitbit-data-with-python-ff145fa10873
- https://python-fitbit.readthedocs.io/en/latest/
- https://tech.gunosy.io/entry/fitbit-activity-notifier#Fitbitのデータを取得するためのトークンを発行する
