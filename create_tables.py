import sqlite3

con = sqlite3.connect('users.db')
cur = con.cursor()

sql = '''
CREATE TABLE IF NOT EXISTS Phones
(phoneID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
contactName VARCHAR(50),
phoneValue VARCHAR(20)
);
'''

cur.execute(sql)
con.commit()
con.close()
