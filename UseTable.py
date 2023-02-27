from CheckTables import Checking
from Tables import Table
from InputChecker import CapitalVariations
cr, db, TableList = Checking()
'''
for y in TableList:
    print(y)
'''
# if "QueryHelper":
# else:
#     ""
# TableName = input("Enter the Table Name:")
TableName = "try"
tb = Table(cr, db, TableName)
if TableName in TableList:
    tb.Describe()
    print(tb.Fields)
    # TableManuplation = input("Do You Want to 'EDIT' the whole Attributes of the Table or Proced to 'MANAGE' the Data in it -> ")
    TableManuplation = "MANAGE"
    while (TableManuplation in CapitalVariations("Edit") ):
        UserInput = input("Do You Want to 'ALTER', 'DELETE' or 'REPLACE' the Table from the Database:")
        if UserInput in CapitalVariations("Alter"):
            tb.Alter()
            break
        elif UserInput in CapitalVariations("Delete"):
            tb.Delete()
            break
        elif UserInput in CapitalVariations("Replace"):
            tb.Replace()
            break
        else:
            print("Please Try Again.")
            continue
    while (TableManuplation in CapitalVariations("Manage") ):
        # UserInput = input("Do You Want to 'ADD', 'UPDATE' or 'READ' Data from the Database:")
        UserInput = "Add"
        if UserInput in CapitalVariations("Add"):
            tb.Add()
            break
        elif UserInput in CapitalVariations("Read"):
            tb.Read()
            break
        elif UserInput in CapitalVariations("Update"):
            tb.Update()
            break
        else:
            print("Please Try Again.")
            continue
else:
    tb.Create()
    # try:
    #     tb.Create(TableName)
    # except:
    #     try:
    #         tb.Replace()
    #     except:
    #         print("There is Some Error in Creating the Table.")
    # finally:
    #         pass
cr.close()
db.close()
