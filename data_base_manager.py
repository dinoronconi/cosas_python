import cx_Oracle

try:

    con = cx_Oracle.connect('dino/dino@127.0.0.1/orcl')
    print("Conectado a Oracle " + con.version)
    miCursorRead = con.cursor()
    miCursorWrite = con.cursor()

    miSQLreadPRUEBA = 'Select * from prueba where campo1= :bvid'
    miSQLwritePRUEBA = "INSERT into Prueba(campo1, campo2) values(':dato1', ':dato2')"

    count = 6
    while True:
        miCursorRead.execute(miSQLreadPRUEBA, bvid=1)
        row = miCursorRead.fetchone()
        print('loop '+str(count)+' datos: ')
        print(row)
        count += 1
        if count >= 1000:
            break
        dato1= count
        dato2= 'campo 2 numero '+str(count)
        miCursorWrite.execute("INSERT into Prueba(campo1, campo2) values(:dato1, :dato2)", (dato1, dato2))

    con.commit()
    miCursorRead.close()
    miCursorWrite.close()
    con.close()

except Exception as e:
    con.rollback()
    miCursorRead.close()
    miCursorWrite.close()
    con.close()
    print('Error! Code: {c}, Message, {m}'.format(c=type(e).__name__, m=str(e)))

""" 

sql = 'select * from SampleQueryTab where id = :bvid'

print("Query results with id = 4")
for row in 

    dato1 = '1'
    dato2 = 'dato campo 2'
    miSQL = "INSERT into Prueba(campo1, campo2) values('"+dato1+"', '"+dato2+"')"
    print(miSQL)
    miCursor.execute(miSQL)
  
    con.commit()


rows = cur.fetchall()

for row in rows:
    print(row)
#  for result in cur:
#     print(result)
cur.close()
con.close()
"""