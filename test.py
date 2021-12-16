import psycopg2 as pg2

try:
    dbconn = pg2.connect(host='localhost',
                         port='5432',
                         dbname='je_test',
                         password='answndms9812*')
    print('connect Success!')
except Exception as e:
    print('Not Connected!')
    print(e)