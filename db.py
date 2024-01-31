import random
import psycopg2

class DB:
    def __init__(self) -> None:
        try:
    # connect to exist database
            self.connection = psycopg2.connect(
                 host="localhost", user="sammy", password="Xn~Izpb91iEckYPPuC@umjhJ", database="shsn"   
            )
            self.connection.autocommit = True
        except Exception as _ex:
            print("[INFO] Error while working with PostgreSQL", _ex)


    def create_db(self):
    
        with self.connection.cursor() as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id          serial PRIMARY KEY,    
                    name        varchar(100) NOT NULL,
                    lastname    varchar(100) NOT NULL,
                    password    varchar(64)  NOT NULL,
                    mail        varchar(100) NOT NULL,
                    mail_active varchar(40)  NOT NULL,
                    mail_status BOOLEAN      DEFAULT false
                );

                CREATE TABLE IF NOT EXISTS musics (
                    id          serial PRIMARY KEY,    
                    name        varchar(100) NOT NULL,
                    albom       varchar(100) NOT NULL,
                    author      varchar(100) NOT NULL,
                    consentration float DEFAULT 0,
                    relax       float DEFAULT 0
                );
                """)
    
            # connection.commit()
            print("[INFO] Table created successfully")
    
    def write(self, table, param, values):
        print(f"""INSERT INTO {table} ({param}) VALUES ({values});""")
        with self.connection.cursor() as cursor:
            cursor.execute(f"""INSERT INTO {table} ({param}) VALUES ({values});""")
            return 1
        return 0

    def read(self, table, param):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f"""SELECT {param} FROM {table}""")
                return cursor.fetchall()
        except:
            return 0
    
    def read_one(self, table, param, values):
        try:
            print(f"""SELECT {param} FROM {table} WHERE {values}""")
            with self.connection.cursor() as cursor:
                cursor.execute(f"""SELECT {param} FROM {table} WHERE {values}""")
                return cursor.fetchone()
        except:
            return 0
        
    def update(self, table, seter, condition):
        try:
            print(f"UPDATE {table} SET {seter} WHERE {condition}")
            with self.connection.cursor() as cursor:
                cursor.execute(f"UPDATE {table} SET {seter} WHERE {condition}")
            return True
        except:
            return False

    def delete(self, table, column, values):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f"DELETE FROM {table} WHERE {column} = '{values}'")
                return 1
        except:
            return 0

    def close(self):
        self.connection.close()
        print("[INFO] PostgreSQL connection closed")

    def registration(self, name, lastname, password, mail, mail_active):
        if self.read_one("users", "mail_status", f"mail = '{mail}'"):
            return False
        print(self.read_one("users", "mail_status", f"mail = '{mail}'"))
        return self.write("users", "name, lastname, password, mail, mail_active", f"'{name}', '{lastname}', '{password}', '{mail}', '{mail_active}'")
    def confirm_mail(self, mail):
        try:
            return self.update("users", "mail_status = 1", f"mail_active = '{mail}'")
        except:
            return False
    def check_credentials(self, mail, password):
        try:
            result = self.read_one("users", "mail_status,password", f"mail = '{mail}' ")
            print(result)
            if result:
                if result[1] == password:
                    return 1
                return False
            return 2
        except Exception as ex:
            print(f"[ERROR] Error while checking credentials: {ex}")
            return False
        
    def musics_yep(self, name, albom, author):
        try:
            return self.write("musics", "name, albom, author", f"'{name}', '{albom}', '{author}'")
        except:
            return False
        
    def get_random_musics(self):
        try:
            return random.choice(list(self.read("musics", f"*")))
        except:
            return False
        
    def get_all_musics(self):
        try:
            return list(self.read("musics", f"*"))
        except:
            return False
        
    def set_reta_music(self, id, relax, consentration):
        try:
            # Assuming self.update returns the updated record
            updated_record = self.update("musics", f"relax = '{relax}', consentration = '{consentration}'", f"id = '{id}'")
            # Check if the update was successful
            if updated_record:
                return updated_record
            else:
                return False
        except Exception as e:
            # Handle the exception, print or log the error for debugging
            print(f"Error: {e}")
            return False

        
    
if __name__ == '__main__':
    db = DB()
    db.create_db()
    # db.registration('lolnam1e', 'lolla1stname', 'lol11234', 'lo1w323l@vk.com', 'lo121ddddddl')
    # db.confirm_mail('lo1l')
    # print(db.read("users where password=`8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92`", "*"))
    # print(db.read_one('users', 'password', f"mail = 'obod495@gmail.com'"))
    # print(db.check_credentials('lo12l@vk.com','lol112344'))
    print(db.get_random_musics())
    print(db.read('musics', "*"))
