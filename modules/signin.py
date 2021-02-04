import bcrypt
import pdb
from flask import request, redirect, url_for
from flask_login import login_user
import app

class Signin:
    @classmethod
    def call(cls):
        email = request.form.get('email')
        user = app.User.query.filter_by(email=email).first()
        if user is None:
            return redirect(url_for('signin'))
        if not bcrypt.checkpw(request.form.get('password').encode(), user.hashed_password):
            return redirect(url_for('signin'))
        
        login_user(user)
        return redirect(url_for('fitbit_registration'))

if __name__ == "__main__":
    call()
