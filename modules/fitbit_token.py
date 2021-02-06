import app, fitbit, pdb
import modules.gather_keys_oauth2 as Oauth2
from flask import request, redirect, url_for
from flask_login import login_user

class FitbitToken:
    @classmethod
    def call(cls):
        user = app.User.query.filter_by(id=int(request.args.get('user_id'))).first()
        target_distance = int(request.args.get('target_distance'))

        if not user.client_id or not user.client_secret or not target_distance:
            return 'not registered'

        REDIRECT_URI = 'http://127.0.0.1:8080/'
        server = Oauth2.OAuth2Server(user.client_id, user.client_secret, redirect_uri=REDIRECT_URI)
        server.browser_authorize()

        user.access_token = str(server.fitbit.client.session.token['access_token'])
        user.refresh_token = str(server.fitbit.client.session.token['refresh_token'])
        user.target_distance = target_distance
        app.db.session.commit()
        login_user(user)
        return 'Registered! Close browser.'

if __name__ == "__main__":
    call()
