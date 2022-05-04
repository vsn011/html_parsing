"""An example of a test module in pytest."""

from config import table_name, holidays_test_list, years_test_list, page_title
from typing import List
from db_conn import db_conn
import pandas as pd


def test_page_title() -> str:
    with open("output/title.txt", "r") as f:
        title = f.read()
    
    assert title == page_title


def test_holidays() -> list:
    with db_conn.begin() as conn:
        df_h = pd.read_sql('select distinct Holiday from {} order by Holiday, Year asc'.format(table_name), conn)
    list_of_holidays = df_h['Holiday'].values.tolist()
    assert holidays_test_list.sort() == list_of_holidays.sort()


def test_years() -> list:
    with db_conn.begin() as conn:
        df_y = pd.read_sql('select distinct Year from {} order by Holiday, Year asc'.format(table_name), conn)
    list_of_years = df_y['Year'].values.tolist()
    assert years_test_list.sort() == list_of_years.sort()


def test_sql() -> int:
    with db_conn.begin() as conn:
        df = pd.read_sql('select count(*) from {}'.format(table_name), conn, columns=[['count']])
        number = int(df.iloc[0,0])
    no_of_records = len(holidays_test_list) * len(years_test_list)
    
    assert no_of_records == number



 