from UseDatabase import ConnectToDB # import UseDatabase
def Checking():
    cr, db = ConnectToDB()
    cr.execute("SHOW TABLES")
    ListOfTables = []
    for y in cr:
        print(str(y[0]))
        ListOfTables.append(str(list(y)[0]))
    return cr, db, ListOfTables
