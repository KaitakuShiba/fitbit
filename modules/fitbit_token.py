import app, fitbit, pdb, os
import modules.gather_keys_oauth2 as Oauth2
from flask import request, redirect, url_for
from flask_login import login_user, current_user
from oauthlib.oauth2.rfc6749.errors import MismatchingStateError, MissingTokenError, InvalidGrantError

class FitbitToken:
    @classmethod
    def call(cls):
        target_distance = float(request.args.get('target_distance'))
        code = request.args.get('code')

        if not current_user.client_id or not current_user.client_secret or not target_distance or not code or not os.getenv('REDIRECT_URI'):
            return 'not registered'
        
        server = Oauth2.OAuth2Server(current_user.client_id, current_user.client_secret, redirect_uri=os.getenv('REDIRECT_URI'))
        try:
            server.fitbit.client.fetch_access_token(code)
        except InvalidGrantError:
            return 'Not regstered! Probably, code is not valid.'
        except MissingTokenError:
            return 'Not regstered! MissingTokenError.'
        except MismatchingStateError:
            return 'Not regstered! MismatchingStateError.'

        current_user.access_token = str(server.fitbit.client.session.token['access_token'])
        current_user.refresh_token = str(server.fitbit.client.session.token['refresh_token'])
        current_user.target_distance = target_distance
        app.db.session.commit()
        login_user(current_user)
        return 'Registered! Close tab.'

if __name__ == "__main__":
    call()
