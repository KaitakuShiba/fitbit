import app, pdb, fitbit, os, base64, json, requests
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from datetime import datetime, date

class CheckDistanceJob:
    @classmethod
    def call(cls):    
        print('starting job..')

        if not os.environ.get('SLACK_CHANNEL') or not os.environ.get('SLACK_BOT_TOKEN'):
            print('not setting env')
            return

        for user in app.User.query.all():
            if not user.client_id or not user.client_secret or not user.access_token or not user.refresh_token or not user.target_distance:
                continue
            if cls._has_already_called_today(user.updated_at):
                continue
            
            auth2_client = fitbit.Fitbit(user.client_id, user.client_secret, oauth2=True, access_token=cls._get_access_token(user), refresh_token=user.refresh_token)
            today = str((datetime.now()).strftime("%Y-%m-%d"))
            try:
                fit_stats_distance = auth2_client.intraday_time_series('activities/distance', base_date=today, detail_level='1min')
            except fitbit.exceptions.HTTPUnauthorized:
                print(f'user_id: {user.id} has invalid token.')
                continue
            
            kms = cls._convert_km(fit_stats_distance['activities-distance'][0]['value'])
            if cls._is_over_target_distance(kms, user.target_distance):
                cls._send_message_to_slack(user, kms)
                user.updated_at = datetime.now()
                app.db.session.commit()
       
        print('updated!')
        return 'updated!'

    def _convert_km(str_miles):
        conv_fac = 0.621371
        return float(str_miles) / conv_fac
    
    def _is_over_target_distance(kms, target_distance):
        return  kms > target_distance

    def _has_already_called_today(updated_at):
        today = datetime.combine(date.today(), datetime.min.time())
        return updated_at >= today

    def _send_message_to_slack(user, kms):
        client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])
        try:            
            text = f'{user.name}さんが目標距離: {user.target_distance}kmを達成しました。現在の距離: {round(kms, 2)}km :100::woman-running::runner::man-running::skin-tone-3:'
            client.chat_postMessage(channel=os.environ['SLACK_CHANNEL'], text=text)
        except SlackApiError as e:
            print(f"Got an error: {e.response['error']}")
        
    def _get_access_token(user):
        # https://dev.fitbit.com/build/reference/web-api/oauth2/#refreshing-tokens
        auth = f'{user.client_id}:{user.client_secret}'
        auth_base64 = base64.b64encode(auth.encode())
        data = {'grant_type': 'refresh_token', 'refresh_token': user.refresh_token}
        url = 'https://api.fitbit.com/oauth2/token'
        header = {'content-type': 'application/x-www-form-urlencoded', 'Authorization': f'Basic {auth_base64.decode()}'}        
        res = requests.post(url , headers=header, data=data)
        return json.loads(res.text)['access_token']
        

if __name__ == "__main__":
    call()
