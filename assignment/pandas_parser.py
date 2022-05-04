import pandas as pd
from config import url, table_name
from db_conn import db_conn
from requests_html import HTMLSession


#we connect to the website and get a list of tables, 3 in total
df = pd.read_html(url, parse_dates=True)

#the desired table is table number 3
columns= ['Holiday', '2022', '2023', '2024']
df = df[2]
df.columns = columns

#we then unpivot columns to turn them into rows
df_t = pd.melt(df, id_vars = ['Holiday'], value_vars=['2022', '2023', '2024'], var_name='Year', value_name='Date')
print(df_t.sort_values(['Holiday', 'Year']))


