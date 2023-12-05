import mysql.connector

#파이썬으로 MySQL에 접속할수 있는 함수.

def get_connection() :
   connection = mysql.connector.connect(
        host = 'yhdb.c1yd9oawbmbu.ap-northeast-2.rds.amazonaws.com',
        database = 'recipe_db',
        user = 'recipe_db_user',
        password = '1004'
   )
   return connection