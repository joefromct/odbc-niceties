import pyodbc
import os
import odbc_niceties as sut
import logging
from pprint import pprint as pp



try:
    conn_string=os.environ['CONN_STRING']
except KeyError:
    raise KeyError("No CONN_STRING string in envorinment?")

def test_version():
    assert sut.__version__ == '0.1.1'


# TODO
sql = """
select 'falcons'  as team_name, 'atlanta' as team_city, 3  as team_wins union all
select 'patriots' as team_name, 'boston'  as team_city, -3 as team_wins union all
select 'eagles'   as team_name, 'philly'  as team_city, 2  as team_wins union all
select 'cowboys'  as team_name, 'dallas'  as team_city, 1  as team_wins """

with pyodbc.connect(conn_string) as conn, \
     conn.cursor() as cur:
    cur.execute(sql)
    res = sut.sql_data(cur)
    sut.make_table(res)
