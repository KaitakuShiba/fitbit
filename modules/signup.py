import bcrypt
import pdb
from flask import request, redirect, url_for
from flask_login import login_user
import app

class Signup:
    @classmethod
    def call(cls):
        email = request.form.get('email')
        client_id = request.form.get('client_id')
        client_secret = request.form.get('client_secret')
        hashed_password = bcrypt.hashpw(request.form.get('password').encode(), bcrypt.gensalt())
        app.db.session.add(app.User(email=email, hashed_password=hashed_password, client_id=client_id, client_secret=client_secret))
        app.db.session.commit()
        user = app.User.query.filter_by(email=email).first()
        login_user(user)
        return redirect(url_for('fitbit_registration'))

if __name__ == "__main__":
    call()
