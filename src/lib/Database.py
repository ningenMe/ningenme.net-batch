import sys
import datetime
import pathlib
import mysql.connector
path = pathlib.Path(__file__).resolve()
sys.path.append(str(path.parent)+'/../conf')
import Env
import Log

class Datebase:
    def __init__(self):
        self.database = mysql.connector.connect(
            host    =Env.MYSQL_HOST,
            port    =Env.MYSQL_PORT,
            db      =Env.MYSQL_DB,
            user    =Env.MYSQL_USER,
            password=Env.MYSQL_PASSWORD,
        )
    
    def __del__(self):
        self.database.close()

    def select(self,query):
        try:
            stmt = self.database.cursor(buffered=True)
            stmt.execute(query)
            rows = stmt.fetchall()
            stmt.close()
        except Exception as e:
            Log.error(e)
            return False
        return rows

    def update(self,query):
        try:
            stmt = self.database.cursor(buffered=True)
            stmt.execute(query)
            self.database.commit()
            stmt.close()
        except Exception as e:
            Log.error(e)
            return False
        return True
