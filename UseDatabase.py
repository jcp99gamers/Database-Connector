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
    # elif DB_Name in CapitalVariations(ListOfDb):
    #     # variations_list = CapitalVariations(ListOfDb)
    #     # for i, sublist in enumerate(AttributeParameter):
    #     #     if AttributeParameter in sublist:
    #     #         index_value = (i, sublist.index(AttributeParameter))
    #     #         val = variations_list[index_value[0]][index_value[1]]
    #     #     else:
    #     #         # print("Not found")
    #     #         continue
    #     # pass*
    else:
        object = CreateDb()
        object.Creating(DB_Name)
    cr , db = Cursor(host, user, password, DB_Name)
    print("-----")
    return cr, db
# ConnectToDB()