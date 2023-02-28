import pandas as pd
import numpy as np
from InputChecker import CapitalVariations
import re
class Initilisation:
    def __init__(self, cr, db, TableName):
        self.cr = cr
        self.db = db
        self.tn = TableName
    def Read_DataFrame(self, Where=True):
        self.df = pd.read_sql('SELECT * FROM '+self.tn+' where '+str(Where), con=self.db)
        return self.df
        pass    
class ReadTable(Initilisation):
    def __init__(self, cr, db, TableName):
        super().__init__(cr, db, TableName)
        # self.df = pd.DataFrame()
        # def __init__(self, cr, db, TableName):
        #     self.cr = cr
        #     self.db = db
        #     self.tn = TableName
        self.cr.execute("DESCRIBE " + self.tn+";")
        result = self.cr.fetchall()
        self.rows = [row for row in result]
        self.Fields = [row[0] for row in self.rows]
        self.Type = [row[1].decode('utf-8') for row in self.rows]
        self.Null = [row[2] for row in self.rows]
        self.Key = [row[3] for row in self.rows]
        self.Default = [row[4] for row in self.rows]
        self.Extra = [row[5] for row in self.rows]
    def Where(self):
        Wherez = input("What Do You Wana Search for in the Database = ")
        self.df = super().Read_DataFrame()
        try:
            Wherez = int(Wherez)
        except:
            search_values = CapitalVariations(Wherez) # create a list of values to search for
            result_series = self.df.applymap(lambda x: x in search_values).any(axis=1) # use applymap and any to get a boolean series indicating which rows contain any of the search values
            result_df = self.df[result_series] # filter the original DataFrame with the boolean series
        else:
            mask = self.df.eq(Wherez).any(axis=1) # Search for the value in the DataFrame
            result_df = self.df[mask] # Filter the DataFrame using boolean indexing
        finally:
            return result_df  #WhereDF = (self.df == Wherez).any().any()
class TableDataManiplation(ReadTable):
    def __init__(self, cr, db, TableName):
        super().__init__(cr, db, TableName)
        self.Fields = self.Fields
        self.corresponding_tuple = tuple(self.Fields)
        self.correspondingFeilds = '(' + ','.join(self.corresponding_tuple) + ')' # self.correspondingFeilds = str(self.corresponding_tuple)
        self.len_corresponding = len(self.Fields)
        self.correspondingValue = r"("
        for s in range(self.len_corresponding):
            if s != self.len_corresponding-1:
                self.correspondingValue = self.correspondingValue +"%s"+"," # self.correspondingValue = self.correspondingValue +"'{}'"+","
            else:
                self.correspondingValue += "%s"# self.correspondingValue += "'{}'" 
        self.correspondingValue += r")"
    def Add(self):
        def Valuez():
            parent_list = []
            '''
            #COUNTING METHOD
            counters = int(input("How Many Rows Would You Like to Add = "))
            for x in range(counters):
                child_listTOtuple = [] # tuplez = ()
                for y in self.corresponding_tuple:
                    val_input = input("Enter the Value of Column "+y+" =")
                    child_listTOtuple.append(val_input)    
                child_listTOtuple = tuple(child_listTOtuple)
                parent_list.append(child_listTOtuple)
            '''
            #DIRECT METHOD
            while True:
                breaker_statement = input("Do You Want to Add More Data to the Database (y/n) :")
                if breaker_statement == "y":
                    pass
                elif breaker_statement == "n":
                    break
                else:
                    print("TRY AGAIN \n")
                    continue
                for y in self.corresponding_tuple:
                    child_listTOtuple = [] # tuplez = ()
                    val_input = input("Enter the Value of Column "+y+" =")
                    child_listTOtuple.append(val_input)    
                child_listTOtuple = tuple(child_listTOtuple)
                parent_list.append(child_listTOtuple)    
            return parent_list
        query = "INSERT INTO "+self.tn+" "+self.correspondingFeilds+" VALUES "+self.correspondingValue+";"
        # print(query)
        valz = Valuez() # valz = [('Holla', "20")]
        self.cr.executemany(query, valz) # [ self.cr.execute(query.format(v[0], v[1])) for v in valz ]
        self.db.commit()
        # print(self.cr.rowcount, "was inserted.")
        pass
    def Update(self):
        super().Read()
        pass
class Creations(Initilisation):
    def __init__(self, cr, db, TableName):
        super().__init__(cr, db, TableName)
    # def __init__(self, cr, db, TableName):
    #     self.cr = cr
    #     self.db = db
    #     self.tn = TableName
    def Create(self):
        ColumnCounter = int(input("How Many Colums Do U Need = "))
        QueryAttributes = ""
        while (0<ColumnCounter): # for x in range(ColumnCounter+1):
            # db_Att_Checker = ["CHAR","TINYTEXT","TEXT","MEDIUMTEXT","LONGTEXT","image","BOOL","BOOLEAN","TINYINT","SMALLINT","MEDIUMINT","BIGINT","FLOAT","DOUBLE","DECIMAL","DEC","numeric","smallmoney","money","real","DATE","DATETIME","datetime2","smalldatetime","datetimeoffset","TIMESTAMP","TIME","YEAR"]
            ToReplaceName = input("What is Column Name = ")
            AttributeName = ToReplaceName.replace(" ", "_")
            while True:
                AttributeParameter = input("What Do U Want the Parameters of this Attribute to be = ")
                if "(" in AttributeParameter or ")" in AttributeParameter:
                    patternz = r'\((\d+)(?:,(\d+))?\)'
                    matcher = re.search(patternz, AttributeParameter)
                    if matcher.group(2):
                        pattern = r"^(\w+)\((.*)\)$"
                        match = re.search(pattern, AttributeParameter)
                        Attribute = match.group(1)
                        Value = match.group(2)
                    else:
                        pattern = r'([\w\s]+)(\([\d]+\))?'
                        match = re.match(pattern, AttributeParameter)
                        Attribute = match.group(1).strip()
                        Value = match.group(2)
                    AttributeParameter = Attribute
                    if (AttributeParameter in CapitalVariations(["String", "Str", "Varchar","Var","CHAR","TEXT"])):
                            AttributeParameter = "VARCHAR"+Value
                            break
                    if (AttributeParameter in CapitalVariations(["DECIMAL","Dec","Float","DOUBLE"])):
                            AttributeParameter = "DECIMAL"+Value
                            break
                    elif (AttributeParameter in CapitalVariations(["TINYTEXT","MEDIUMTEXT","LONGTEXT",'TINYINT', 'DATETIME', 'BOOLEAN', 'REAL', 'VARBINARY', 'TIMESTAMP', 'YEAR', 'datetimeoffset', 'FLOAT', 'BOOL', 'BINARY', 'datetime2', 'DOUBLE', 'BIGINT', 'ENUM', 'smalldatetime', 'DATE', 'PRECISION', 'INT', 'TIME', 'SET', 'image', 'SMALLINT', 'BLOB'])):
                        variations_list = CapitalVariations(["TINYTEXT","MEDIUMTEXT","LONGTEXT",'TINYINT', 'DATETIME', 'BOOLEAN', 'REAL', 'VARBINARY', 'TIMESTAMP', 'YEAR', 'datetimeoffset', 'FLOAT', 'BOOL', 'BINARY', 'datetime2', 'DOUBLE', 'BIGINT', 'ENUM', 'smalldatetime', 'DATE', 'PRECISION', 'INT', 'TIME', 'SET', 'image', 'SMALLINT', 'BLOB'])
                        for i, sublist in enumerate(AttributeParameter):
                            if AttributeParameter in sublist:
                                index_value = (i, sublist.index(AttributeParameter))
                                val = variations_list[index_value[0]][index_value[1]]
                                VAL = val.upper()
                                AttributeParameter = VAL + Value
                                break
                            else:
                                # print("Not found")
                                continue
                else:
                    # Split the string at the first space character
                    Attribute, value = AttributeParameter.split(' ', 1)
                    # pattern = r'([\w\s]+)([\s]+[\w\s]+)'
                    # match = re.match(pattern, AttributeParameter)
                    # try:
                    #     Attribute = match.group(1).strip()
                    #     Value = match.group(2).strip()
                    # except:
                    #     print("Perhaps You Forgot Something.")
                    #     continue
                    Value = value.upper()
                    AttributeParameter = Attribute
                    if (AttributeParameter in CapitalVariations(["String", "Str", "Varchar","Var","CHAR","TEXT"])):
                            AttributeParameter = "VARCHAR (255) "+Value
                            break
                    elif (AttributeParameter in CapitalVariations(["DECIMAL","Dec","Float","DOUBLE"])):
                            AttributeParameter = "DECIMAL (35,25) "+Value
                            break
                    if (AttributeParameter in CapitalVariations(["int","Integer"])):
                        AttributeParameter = "INT "+Value
                        break
                    # if (AttributeParameter in CapitalVariations("int") or AttributeParameter in CapitalVariations("Integer")):
                    #     AttributeParameter = "INT "+Value
                    #     break
                    elif (AttributeParameter in CapitalVariations(["TINYTEXT","MEDIUMTEXT","LONGTEXT",'TINYINT', 'DATETIME', 'BOOLEAN', 'REAL', 'VARBINARY', 'TIMESTAMP', 'YEAR', 'datetimeoffset', 'FLOAT', 'BOOL', 'BINARY', 'datetime2', 'DOUBLE', 'BIGINT', 'ENUM', 'smalldatetime', 'DATE', 'PRECISION', 'INT', 'TIME', 'SET', 'image', 'SMALLINT', 'BLOB'])):
                        variations_list = CapitalVariations(["TINYTEXT","MEDIUMTEXT","LONGTEXT",'TINYINT', 'DATETIME', 'BOOLEAN', 'REAL', 'VARBINARY', 'TIMESTAMP', 'YEAR', 'datetimeoffset', 'FLOAT', 'BOOL', 'BINARY', 'datetime2', 'DOUBLE', 'BIGINT', 'ENUM', 'smalldatetime', 'DATE', 'PRECISION', 'INT', 'TIME', 'SET', 'image', 'SMALLINT', 'BLOB'])
                        for i, sublist in enumerate(AttributeParameter):
                            if AttributeParameter in sublist:
                                index_value = (i, sublist.index(AttributeParameter))
                                val = variations_list[index_value[0]][index_value[1]]
                                VAL = val.upper()
                                AttributeParameter = VAL+" "+Value
                                break
                            else:
                                # print("Not found")
                                continue
            if (ColumnCounter != 1):
                QueryAttributes = QueryAttributes+AttributeName+" "+AttributeParameter+","
            else:
                QueryAttributes = QueryAttributes+AttributeName+" "+AttributeParameter
            ColumnCounter -= 1
        # Attributes OF Varchar, Int, Etc...
        self.cr.execute(r"CREATE TABLE IF NOT EXISTS "+self.tn+r"("+QueryAttributes+r");")
        pass
    def Alter(self):
        # with Attributes also
        pass
    def Delete(self):
        #ToDo,...
        pass   
class Replace(Creations):
    def __init__(self, cr, db, TableName):
        super().__init__(cr, db, TableName)
    def Replace(self):
        #Copy Data to Pandas
        super().Delete()
        super().Create()
class Table(Replace,TableDataManiplation):
    def __init__(self, cr, db, TableName):
        Replace.__init__(self,cr, db, TableName)
        TableDataManiplation.__init__(self,cr, db, TableName)
    def Describe(self):
        self.cr.execute("DESCRIBE " + self.tn+";")
        result = self.cr.fetchall()
        self.rows = [row for row in result]
        self.Fields = [row[0] for row in self.rows]
        self.Type = [row[1].decode('utf-8') for row in self.rows]
        self.Null = [row[2] for row in self.rows]
        self.Key = [row[3] for row in self.rows]
        self.Default = [row[4] for row in self.rows]
        self.Extra = [row[5] for row in self.rows]
        

