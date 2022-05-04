from get_holidays import GetPublicHolidays
from config import url, columns, table_name
from pprint import pprint
import pandas as pd
from db_conn import db_conn


# getting Public Holidays Table Data from url
fl = GetPublicHolidays(url)

final_list = fl.get_final_table()
pprint(final_list)


# writing data to SQLite with help of Pandas DF
df = pd.DataFrame(final_list, columns=columns)
with db_conn.begin() as conn:
    df.to_sql(name=table_name, con=conn, if_exists='replace', method='multi', index=False)