import psycopg2
conn = psycopg2.connect(host = "localhost",port = 5432,user ='dbo',database = 'postgres')
cur = conn.cursor()
cur.execute("SELECT * from hw_a  where sn not in (select sn from hw_b);")
rows = cur.fetchall()        
print(rows)
for i in rows:
    print(i)
conn.commit()
cur.close()
conn.close()
