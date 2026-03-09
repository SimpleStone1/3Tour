import sqlite3 as sq

class bd:
    def __init__(self):
        self.db_name = '3tour.db'
        self.rectangles = {}
        self.table = ['ID', 'X1', 'X2', 'Y1', 'Y2']
    
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

    def update(self, id, x1=None, x2=None, y1=None, y2=None):
        try:
            with sq.connect(self.db_name) as con:
                cur = con.cursor()
                
                updates = []
                params = []
                
                if x1 is not None:
                    updates.append("X1 = ?")
                    params.append(x1)
                if x2 is not None:
                    updates.append("X2 = ?")
                    params.append(x2)
                if y1 is not None:
                    updates.append("Y1 = ?")
                    params.append(y1)
                if y2 is not None:
                    updates.append("Y2 = ?")
                    params.append(y2)
                
                if not updates:
                    print("Нет данных для обновления")
                    return
                query = f"UPDATE RECTANGLES SET {', '.join(updates)} WHERE ID = ?"
                params.append(id)
                
                cur.execute(query, params)
                con.commit()
        except Exception as e:
            print(f'Ошибка БД при обновлении: {e}')
if __name__ == '__main__':
    bd1 = bd()
    bd1.create()
    bd1.load()