from ConnectToMySQL import Cursor
from ConnectVals import host, user, password
class CreateDb():
    def Creating(self, DB_Name):
        cr , db = Cursor(host, user, password)
        cr.execute("CREATE DATABASE IF NOT EXISTS "+DB_Name+";")
        #CLOSE
        cr.close()
        db.close()