import pymysql

db_host = 'instance-cym.c3qmek8e2dph.us-east-2.rds.amazonaws.com'
db_user = 'admin'
db_password = '12345678'
db_database = 'db_flupets'
db_table = 'persona'

def connectionSQL():
    try:
        connection_sql = pymysql.connect(
            host = db_host,
            user = db_user,
            password = db_password,
            database = db_database
        )
        print("Successfull connection to the database")
        return connection_sql
    except:
        print("Error connecting to the database")
        return None
    
def add_user(id, name, email, phone, petName, pets, birthday):
    instruction_sql = "INSERT INTO " + db_table + " (id, name, email, phone, petName, pets, birthday) VALUES ("+id+", '"+name+"', '"+email+"', "+phone+", '"+petName+"', '"+pets+"', '"+birthday+"')"
    connection_sql = connectionSQL()
    try:
        if connection_sql != None:
            cursor = connection_sql.cursor()
            cursor.execute(instruction_sql)
            connection_sql.commit()
            print("User added")
            return True
        else:
            print("Error connecting to the database")
            return False
    except Exception as err:
        print(err)
        return False
        
def consult_user(id):
    instruction_sql = "SELECT * FROM " + db_table + " WHERE id="+id
    print(instruction_sql)
    connection_sql = connectionSQL()
    try:
        if connection_sql != None:
            cursor = connection_sql.cursor()
            cursor.execute(instruction_sql)
            result_data = cursor.fetchall()
            print(result_data)
            if not result_data:
                print("User not registered")
                return False
            return result_data
        else:
            print("Error connecting to the database")
            return False
    except Exception as err:
        print(err)
        return False