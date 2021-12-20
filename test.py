import psycopg2 as pg2
'''
Description:
    DB connect 체크하는 test 파일
'''
try:
    dbconn = pg2.connect(host='localhost',
                         port='5432',
                         dbname='je_test',
                         password='answndms9812*')
    print('connect Success!')
except Exception as e:
    print('Not Connected!')
    print(e)