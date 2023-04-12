import mysql.connector
from datetime import datetime
from game_database.utils import format_ranking

class Database():
    def __init__(self):
        self.connection = mysql.connector.connect(
            host = "localhost",
            user = "maxuser",
            password = "toor",
            database = "game_db_construct"
        )
        self.cursor = self.connection.cursor()

    def close_connection(self):
        try:
            self.connection.close()
            self.cursor.close()
            return {
                "status":"Ok",
                "message":""
            }
        except Exception as e:
            return {
                "status":"Error",
                "message":e
            }

    def pegar_ultimo_id(self):
        try:
            self.cursor.execute("select * from users where 1 = 1")
            result = self.cursor.fetchall()
            self.connection.commit()
            return {
                "status":"Ok",
                "message":"",
                "ultimo_id":result[0][0]
            }
        except Exception as e:
            return {
                "status":"Error",
                "message":e,
                "ultimo_id":""
            }
        
    def create_user(self, user_name: str):
        try:
            query = f"INSERT INTO users(user_name, created_at, updated_at, experience) VALUES ('{user_name}', '{datetime.now()}', '{datetime.now()}', 0);"
            self.cursor.execute(query)
            self.connection.commit()
            return {
                "status":"Ok",
                "message":f"Usuário {user_name} criado com sucesso."
            }
        except Exception as e:
            return {
                "status":"Error",
                "message":e
            }
        
    def add_experience(self, user_name: str, experience_amount: int):
        try:
            query = f"UPDATE users SET users.experience = users.experience + {experience_amount} WHERE users.user_name = '{user_name}';"
            self.cursor.execute(query)
            self.connection.commit()
            return {
                "status":"Ok",
                "message":f"Adicionado {experience_amount} ao usuário {user_name}."
            }
        except Exception as e:
            return {
                "status":"Error",
                "message":e
            }
        
    def remove_experience(self, user_name: str, experience_amount: int):
        try:
            query = f"UPDATE users SET users.experience = users.experience - {experience_amount} WHERE users.user_name = '{user_name}';"
            self.cursor.execute(query)
            self.connection.commit()
            return {
                "status":"Ok",
                "message":f"Removido {experience_amount} do usuário {user_name}."
            }
        except Exception as e:
            return {
                "status":"Error",
                "message":e
            }
        
    def get_experience(self, user_name: str):
        try:
            self.cursor.execute(f"SELECT users.experience FROM users WHERE users.user_name = '{user_name}';")
            result = self.cursor.fetchall()
            self.connection.commit()
            return {
                "status":"Ok",
                "message":"",
                "user_experience":int(result[0][0])
            }
        except Exception as e:
            return {
                "status":"Error",
                "message":e,
                "user_experience":""
            }
        


    def add_ranking(self, user_name: str, new_experience: int):
        try:
            query = f"INSERT INTO ranking(created_at, new_experience, user_id, user_name) VALUES ('{datetime.now()}', {new_experience}, (SELECT user_id FROM users WHERE users.user_name = '{user_name}'), '{user_name}');"
            self.cursor.execute(query)
            self.connection.commit()
            return {
                "status":"Ok",
                "message":f"Inserido {user_name} ao ranking"
            }
        except Exception as e:
            return {
                "status":"Error",
                "message":e
            }
        
    def get_ranking(self):
        try:
            self.cursor.execute(f"SELECT * FROM ranking WHERE 1 = 1 ORDER BY ranking.new_experience DESC LIMIT 5;")
            result = self.cursor.fetchall()
            self.connection.commit()
            result = format_ranking(result)
            return {
                "status":"Ok",
                "message":"",
                "ranking":result
            }
        except Exception as e:
            return {
                "status":"Error",
                "message":e,
                "ranking":""
            }
        
if __name__ == "__main__":
    db = Database()
    print(db.get_ranking()["ranking"])