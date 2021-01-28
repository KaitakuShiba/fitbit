import pdb
import sqlite3
from flask import request

class FitbirApiRegistration:
    @classmethod
    def call(cls):        
        params = request.form
        params.get('client_id')
        conn = sqlite3.connect('fitbit.db')
        return 'success'

if __name__ == "__main__":
    call()
