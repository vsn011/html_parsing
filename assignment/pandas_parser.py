import pandas as pd
from config import url
#import sqlite3
from sqlalchemy import create_engine as ce


db_conn = ce('sqlite:///datasets/holidays.db')

#we connect to the website and get a list of tables
df = pd.read_html(url, parse_dates=True)

#the desired table is table number 3
columns= ['Holliday', '2022', '2023', '2024']
df = df[2]
df.columns = columns

#we then unpivot columns to turn them into rows
df_t = pd.melt(df, id_vars = ['Holliday'], value_vars=['2022', '2023', '2024'], var_name='Year', value_name='Date')
#print(df_t.sort_values(['Holliday', 'Year']))


df_t.to_sql(name='holidays', con=db_conn)

p2 = pd.read_sql('select * from holidays where order by Holliday, Year', db_conn)

print(p2)