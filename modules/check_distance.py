import app, pdb, fitbit, datetime

class CheckDistanceJob:
    @classmethod
    def call(cls):
        users = app.User.query.all()
        for user in users:
            if not user.client_id or not user.client_secret or not user.access_token or not user.refresh_token or not user.target_distance:
                continue
            
            auth2_client = fitbit.Fitbit(user.client_id, user.client_secret, oauth2=True, access_token=user.access_token, refresh_token=user.refresh_token)
            # 今までの時間にする
            yesterday = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))      
            try:
                fit_stats_distance = auth2_client.intraday_time_series('activities/distance', base_date=yesterday, detail_level='1min')
            except fitbit.exceptions.HTTPUnauthorized:
                print(f'user_id: {user.id} has invalid token.')
                continue
            
            kms = cls._convert_km(fit_stats_distance['activities-distance'][0]['value'])
            if cls._is_over_target_distance(kms, user.target_distance):
                 cls._send_message_to_slack()

        return 'updated!'

    def _convert_km(str_miles):
        conv_fac = 0.621371
        return float(str_miles) / conv_fac
    
    def _is_over_target_distance(kms, target_distance):
        return  kms > target_distance

    def _send_message_to_slack():
        print('slack')

if __name__ == "__main__":
    call()
