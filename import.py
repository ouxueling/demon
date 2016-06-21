import psycopg2

conn = psycopg2.connect(host = "localhost",port = 5432,user ='dbo',database = 'postgres')
cur = conn.cursor()
cur.execute("CREATE TABLE hw_a(sn integer,name varchar,PRIMARY KEY(sn));")
cur.execute("CREATE TABLE hw_b(sn integer,name varchar,PRIMARY KEY(sn));")

cur.execute("insert into hw_a(sn, name) values (%s, %s)",(10,'A10'))
cur.execute("insert into hw_a(sn, name) values (%s, %s)",(20,'A20'))
cur.execute("insert into hw_a(sn, name) values (%s, %s)",(30,'A30'))
cur.execute("insert into hw_a(sn, name) values (%s, %s)",(40,'A40'))
cur.execute("insert into hw_a(sn, name) values (%s, %s)",(50,'A50'))
cur.execute("insert into hw_a(sn, name) values (%s, %s)",(60,'A60'))

cur.execute("insert into hw_b(sn, name) values (%s, %s)",(40,"B40"))
cur.execute("insert into hw_b(sn, name) values (%s, %s)",(50,"B50"))
cur.execute("insert into hw_b(sn, name) values (%s, %s)",(60,"B60"))
cur.execute("insert into hw_b(sn, name) values (%s, %s)",(70,"B70"))
cur.execute("insert into hw_b(sn, name) values (%s, %s)",(80,"B80"))


cur.execute("SELECT * from hw_a  where sn not in (select sn from hw_b);")
rows = cur.fetchall()        
for i in rows:
    print(i)
conn.commit()
cur.close()
conn.close()


