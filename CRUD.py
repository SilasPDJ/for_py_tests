import mysql.connector
from mysql import connector
# connector.connect()
conexao = connector.connect(
    host='localhost',
    user='root',
    password='',
    database='empresa_eng'
)
cursor = conexao.cursor()
print(cursor)
# pip install mysql-connector.python
