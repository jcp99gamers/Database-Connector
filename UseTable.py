from CheckTables import Checking
from Tables import Table, Replace
from InputChecker import CapitalVariations
cr, db, TableList = Checking()
for y in TableList:
    print(y)
# if "QueryHelper":
# else:
TableName = input("Enter the Table Name:")
# tb = Table(cr, db, TableName)
if TableName in TableList:
    tb = Table(cr, db, TableName)
    tb.Describe()
    print(tb.Fields)
    TableManuplation = input("Do You Want to 'EDIT' the whole Attributes of the Table or Proced to 'MANAGE' the Data in it -> ")
    while (TableManuplation in CapitalVariations("Edit") ):
        UserInput = input("Do You Want to 'ALTER', 'DELETE' or 'REPLACE' the Table from the Database:")
        if UserInput in CapitalVariations("Alter"):
            tb.Alter()
            break
        elif UserInput in CapitalVariations("Delete"):
            try:
                tb.Delete()
            except Exception as e:
                print(Exception)
            break
        elif UserInput in CapitalVariations("Replace"):
            tb.Replace()
            break
        else:
            print("Please Try Again.")
            continue
    while (TableManuplation in CapitalVariations("Manage") ):
        UserInput = input("Do You Want to 'ADD', 'UPDATE' or 'READ' Data from the Database:")
        if UserInput in CapitalVariations("Add"):
            tb.Add()
            break
        elif UserInput in CapitalVariations("Read"):
            while True:
                UzerInzput = input("Do You Want to 'READ' the Data or Search 'WHERE' a Particualar Data Exists in the Table =")
                if(UzerInzput in CapitalVariations("READ")):
                    print(tb.Read_DataFrame())
                    break
                elif(UzerInzput in CapitalVariations("WHERE")):
                    print(tb.Where())
                    break
                else:
                    print("TRY AGAIN")
                    continue
            break
        elif UserInput in CapitalVariations("Update"):
            tb.Update()
            break
        else:
            print("Please Try Again.")
            continue
else:
    tb = Replace(cr, db, TableName)
    tb.Create()
cr.close()
db.close()
