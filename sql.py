# SQL Alchemy Test
from sqlalchemy import create_engine
import os

dcuser = os.environ.get('DCUSER')
dcpass = os.environ.get('DCPASS')
dcip   = os.environ.get('DCIP')
dcdb   = os.environ.get('DCDB')
db_connection = "postgres://{}:{}@{}/{}"
db_connection = db_connection.format(dcuser, dcpass, dcip, dcdb)

db = create_engine(db_connection)
statement = input()
result = db.execute(statement)
for row in result:
    print(row)
