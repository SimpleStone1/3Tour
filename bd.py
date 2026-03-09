import sqlite3 as sq

class bd:
    def __init__(self):
        self.db_name = '3tour.db'
        self.rectangles = {}
    
    def create(self):
        try:
            with sq.connect(self.db_name) as con:
                cur = con.cursor()
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS RECTANGLES(
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                X1 REAL,
                                X2 REAL,
                                Y1 REAL,
                                Y2 REAL
                                )
                """)
                con.commit()
        except Exception as e:
            print(f'Ошибка БД {e}')

    def load(self):
        try:
            with sq.connect(self.db_name) as con:
                cur = con.cursor()
                cur.execute("""
                    SELECT * FROM RECTANGLES
                """)
                lines = cur.fetchall()
                for line  in enumerate(lines):
                    self.rectangles[line[0]] = line[1]
        except Exception as e:
            print(f'Ошибка БД {e}')
    def add_item(self, id, x1, y1, x2, y2):
        try:
            with sq.connect(self.db_name) as con:
                cur = con.cursor()
                cur.execute("""
                    INSERT OR IGNORE INTO RECTANGLES VALUES (?, ?, ?, ?, ?)
                """, (id, x1, x2, y1, y2))
                con.commit()
        except Exception as e:
            print(f'Ошибка БД {e}')
    
    def delete(self, id):
        try:
            with sq.connect(self.db_name) as con:
                cur = con.cursor()
                cur.execute("""
                    DELETE FROM RECTANGLES WHERE ID = ?
                """, (id,))
        except Exception as e:
            print(f'Ошибка БД {e}')

if __name__ == '__main__':
    bd1 = bd()
    bd1.create()
    bd1.load()
    bd1.add_item(3, 22.0, 33.0, 23.0, 44.0)
    bd1.delete(1)