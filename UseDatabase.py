from ConnectToMySQL import Cursor
from CheckDatabases import ListOfDb
from CreateADatabase import CreateDb
from InputChecker import CapitalVariations
from ConnectVals import host, user, password
def ConnectToDB():
    print("\n")
    import CheckDatabases
    print("\n")
    print("-----")
    DB_Name = input("Enter the Name of the Database You Want to Use = ")
    if DB_Name in ListOfDb:     
        pass    
    elif DB_Name in CapitalVariations(ListOfDb):
        capital_variations = CapitalVariations(ListOfDb)
        if DB_Name in capital_variations:
            Common = list(set(ListOfDb) & set(CapitalVariations(DB_Name)))
            DB_Name = Common[0]
    else:
        object = CreateDb()
        object.Creating(DB_Name)
    cr , db = Cursor(host, user, password, DB_Name)
    print("-----")
    return cr, db
# ConnectToDB()