import os
import pdb
import fitbit
import modules.gather_keys_oauth2 as Oauth2
import datetime

class Fitbit:
    @classmethod
    def call(cls):
        if os.getenv('CLIENT_ID') is None or os.getenv('CLIENT_SECRET') is None:
            return 'not registerd!!', 403

        # TODO:後でDBから取得できるようにする
        CLIENT_ID = os.getenv('CLIENT_ID')
        CLIENT_SECRET = os.getenv('CLIENT_SECRET')
        REDIRECT_URI = 'http://127.0.0.1:8080/'

        server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET, redirect_uri=REDIRECT_URI)
        server.browser_authorize()

        ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
        REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
        auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

        # https://dev.fitbit.com/build/reference/web-api/activity/
        yesterday = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
        fit_stats_distance = auth2_client.intraday_time_series('activities/distance', base_date=yesterday, detail_level='1min')
        return fit_stats_distance['activities-distance'][0]['value'], 200

if __name__ == "__main__":
    call()
