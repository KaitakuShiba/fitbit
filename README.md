## 前提
Python 3.9.1
Flask 1.1.2

## 概要
```bash
$ pip install pipenv
$ cd this_project
$ pipenv --python 3.9
# install package
$ pipenv install -r ./requirements/dev.txt
# run dev env server
$ export FLASK_ENV=development
$ pipenv run flask run
$ curl http://localhost:5000
Hello, World!
# version
$ pipenv run python --version
# testing
$ pipenv run pytest
```
