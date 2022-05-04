from db_conn import db_conn
import pandas as pd
from config import table_name


with db_conn.begin() as conn:
    df = pd.read_sql('select * from {} order by Holiday, Year asc'.format(table_name), conn)

print(df)
