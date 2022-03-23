from sqlite3 import connect
import json

class Database():
    def __init__(self, count = 0):
        self.conn = connect("Database.db")
        self.CreateTable()
        self.count = count
        self.version_json = []

    def CreateTable(self):
        cursor = self.conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS versions (id INTEGER PRIMARY KEY AUTOINCREMENT, version TEXT)")
        self.conn.commit()
        cursor.close()

    # def ReadTable(self):
    #     cursor = self.conn.cursor()
    #     cursor.execute("SELECT version FROM versions")
    #     elem = cursor.fetchall()
    #     for stack in elem:
    #         print(self.count, "version: ", json.loads(stack[0]))
    #         self.count += 1
    #
    #     cursor.close()

    def Insert_in_Table(self, data):
        cursor = self.conn.cursor()
        cursor.execute(f"""INSERT INTO versions (version) VALUES ('{data}')""")
        self.conn.commit()
        cursor.close()

    def lastVersion(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT version FROM versions WHERE id = (SELECT MAX(id) FROM versions);")
        last_version_json = json.dumps(cursor.fetchone())
        last_version = json.loads(last_version_json)
        self.conn.commit()
        cursor.close()
        return last_version

    def id(self):
        cursor = self.conn.cursor()
        list_id = [str(i)[1:-2] for i in cursor.execute("SELECT id FROM versions")]
        cursor.close()
        # print(list_id)
        return list_id

    def lastID(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id FROM versions WHERE id = (SELECT MAX(id) FROM versions)")
        last_ID = cursor.fetchone()
        self.conn.commit()
        cursor.close()
        return last_ID

    def select(self, id):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT version FROM versions WHERE id = ('{id}')")
        select_json = json.dumps(cursor.fetchone())
        select = json.loads(select_json)
        if select != None:
            select2 = select[0][1:-1]
        else:
            return None
        self.conn.commit()
        cursor.close()
        return select2


# if __name__ == '__main__':
#     db = Database()
#     st = db.select(1)
#     print(st[0][1:-1])