from flask import request, redirect, url_for, render_template
from flask_login import login_user
from sqlalchemy.exc import IntegrityError, InvalidRequestError
import app, bcrypt

class Signup:
    @classmethod
    def call(cls):
        name = request.form.get('name')
        hashed_password = bcrypt.hashpw(request.form.get('password').encode(), bcrypt.gensalt())
        client_id = request.form.get('client_id')
        client_secret = request.form.get('client_secret')
        try:
            app.db.session.add(app.User(name=name, hashed_password=hashed_password, client_id=client_id, client_secret=client_secret))
            app.db.session.commit()
        except (IntegrityError, InvalidRequestError) as e:
            print(e)
            app.db.session.rollback()
            return render_template('signup.html', message='サインアップできませんでした')
        user = app.User.query.filter_by(name=name).first()
        login_user(user)
        return redirect(url_for('fitbit_registration'))

if __name__ == "__main__":
    call()
