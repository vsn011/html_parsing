"""An example of a test module in pytest."""

from get_holidays import GetPublicHolidays
from config import url, columns, table_name, holidays_test_list, years_test_list, no_of_records, page_title
from typing import List
from db_conn import db_conn
import pandas as pd




fl = GetPublicHolidays(url)

def test_page_title() -> str:
    title = fl.get_page_title()
    assert title == page_title


def test_holidays() -> list:
    list_of_holidays = fl.get_table_data()[1]
    assert holidays_test_list.sort() == list_of_holidays.sort()


def test_years() -> list:
    list_of_years = fl.get_table_data()[1]
    assert years_test_list.sort() == list_of_years.sort()


def test_number_of_records() -> int:
    final_list = fl.get_final_table()
    assert no_of_records == len(final_list)


def test_sql() -> int:
    with db_conn.begin() as conn:
        df = pd.read_sql('select count(*) from {}'.format(table_name), conn, columns=[['count']])
        number = int(df.iloc[0,0])
    assert no_of_records == number



 