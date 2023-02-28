import sys
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
    words = DB_Name.split()
    if words[0] in CapitalVariations(["Delete","Del","Dele","Delet","Drop","Remove"]) or words[0] == "-":
        cr , db = Cursor(host, user, password)
        rest_of_string = ' '.join(words[1:]) # Join the remaining words back into a string as the second value
        # convert both user input and list elements to lowercase
        user_input_lower = rest_of_string.lower()
        my_list_lower = [x.lower() for x in ListOfDb]
        # check if user input exists in the list
        if user_input_lower in my_list_lower:
            # if it does, find the corresponding list value and return it
            index = my_list_lower.index(user_input_lower)
            corresponding_value = ListOfDb[index]
            # print(corresponding_value)
            cr.execute("DROP DATABASE IF EXISTS "+corresponding_value+";")
            print("DATABSE "+corresponding_value+" -> Has been Deleted.")
        else:
            print("The value you entered does not exist in the list.") # if it doesn't, inform the user that the value doesn't exist in the list
        sys.exit(1) # Exit with a status code of 1
    if DB_Name in ListOfDb:     
        pass    
    elif DB_Name in CapitalVariations(ListOfDb):
        capital_variations = CapitalVariations(ListOfDb)
        # if DB_Name in capital_variations:
        Common = list(set(ListOfDb) & set(CapitalVariations(DB_Name)))
        DB_Name = Common[0]
    else:
        object = CreateDb()
        object.Creating(DB_Name)
    cr , db = Cursor(host, user, password, DB_Name)
    print("-----")
    return cr, db
# ConnectToDB()