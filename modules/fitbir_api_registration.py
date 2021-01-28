import pdb, sqlite3
from flask import request

class FitbirApiRegistration:
    @classmethod
    def call(cls):
        # あとで使う: https://flask.palletsprojects.com/en/1.1.x/patterns/sqlalchemy/
        params = request.form
        client_id = params.get('client_id')
        client_secret = params.get('client_secret')
        target_distance = params.get('target_distance')
        conn = sqlite3.connect('fitbit.db')
        cur = conn.cursor()
        sql = f"INSERT INTO Users(client_id, client_secret, target_distance) values('{client_id}', '{client_secret}', '{target_distance}')"
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
        return 'success'

if __name__ == "__main__":
    call()
