from ConnectToMySQL import Cursor
from ConnectVals import host, user, password
cr , db = Cursor(host,user,password)
cr.execute("SHOW DATABASES")
ListOfDb = []
for x in cr:
    print(str(x[0])) # print(x)
    ListOfDb.append(str(list(x)[0]))
#CLOSE
cr.close()
db.close()