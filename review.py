import sqlite3 as sq
import datetime as dt
import pandas as pd
import sys

db = 'reviews.db'
table = 'reviews'
def add_review(title,material_location):
    '''
    add a review to the system
    title: the title of the review
    material_location: location of the review materials
    '''
    conn = sq.connect(db)
    c = conn.cursor()
    now = dt.datetime.now()
    d1 = dt.timedelta(days=1) + now
    d7 = dt.timedelta(days=7) + now
    d30 = dt.timedelta(days=30) + now
    d180 = dt.timedelta(days=180) + now
    d360 = dt.timedelta(days=360) + now
    study_date = now.strftime('%Y-%m-%d')
    for d in [d1,d7,d30,d180,d360]:
        d = d.strftime('%Y-%m-%d')
        sql = 'insert into {} (date,title,material_location,study_date) values ("{}","{}","{}","{}")'.format(table,d,title,material_location,study_date)
        c.execute(sql)
    conn.commit()
    conn.close()
def reviews_today():
    today = dt.datetime.now().strftime('%Y-%m-%d')
    #yesterday = now - dt.timedelta(days=1)
    #tomorrow = now + dt.timedelta(days=1)
    conn = sq.connect(db)
    df = pd.read_sql('select * from {} where date = "{}"'.format(table,today),conn)
    conn.close()
    return df

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 0:
        print(reviews_today())
    else:
        if len(args)==1:
            add_review(args[0],'')
        else:
            add_review(args[0],args[1])

