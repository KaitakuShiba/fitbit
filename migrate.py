from app import db

def create_db():
    db.create_all()
    print('migrate completed!')

create_db()
