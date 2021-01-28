import sqlite3

def call():
    DB_NAME = 'fitbit.db'
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    conn.execute('''CREATE TABLE users(
        id INTEGER PRIMARY KEY AUTOINCREMENT, client_id STRING, client_secret STRING, target_distance INTEGER)'''
    )
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    call()
