from sqlalchemy import create_engine as ce
from config import table_name, db


db_conn = ce('sqlite:///{0}/{1}.db'.format(db, table_name))

