import os
import logging
from database.sql_commands import sqlite_connection


#logger = logging.getLogger(__name__)

def is_exist_db(db_path):
    return os.path.isfile(db_path)

def create_db(db_path):
    conn = sqlite_connection(db_path)
    conn = sql_table(conn)
    conn.close()

def sql_table(connector):
    c = connector.cursor()
    c = sql_create_table(c, 'Year')
    c = sql_create_table(c, 'Grade', 'FLOAT')
    c = sql_create_table(c, 'Status')
    c = sql_create_table(c, 'Interest', 'TEXT')
    c = sql_create_table(c, 'Actor', 'TEXT')
    c = sql_create_main_table(c, 'Movies')
    c = sql_create_intertable(c, 'Movies_Status', 'Name')
    c = sql_create_intertable(c, 'Movies_Interest', 'Name')
    c = sql_create_intertable(c, 'Movies_Actor', 'Name')
    c = sql_create_main_table(c, 'Serials')
    c = sql_create_intertable(c, 'Serials_Status', 'Name')
    c = sql_create_intertable(c, 'Serials_Interest', 'Name')
    c = sql_create_intertable(c, 'Serials_Actor', 'Name')

    connector.commit()
    return connector

def sql_create_table(cursor, table_name, value_type='INTEGER'):
    query = ''' CREATE TABLE {} (
                ID{} INTEGER PRIMARY KEY AUTOINCREMENT,
                Value {} NOT NULL)'''.format(table_name, table_name, value_type)
    cursor.execute(query)
    return cursor

def sql_create_intertable(cursor, table_name, id_in_main_table):
    main_table_name = table_name.split('_')[0]
    id_column = 'ID' + table_name.split('_')[-1]
    side_table_name = table_name.split('_')[-1]

    query = ''' CREATE TABLE {} (
                {} TEXT REFERENCES {}({}),
                {} INTEGER REFERENCES {}({}))
                '''.format(table_name, id_in_main_table, main_table_name,
                           id_in_main_table, id_column, side_table_name,
                           id_column)
    cursor.execute(query)
    return cursor

def sql_create_main_table(cursor, table_name):
    query = ''' CREATE TABLE {} (
                Name TEXT PRIMARY KEY NOT NULL,
                IDYear INTEGER REFERENCES Year(IDYear),
                IDGrade INTEGER REFERENCES Grade(IDGrade),
                Number_of_views INTEGER)'''.format(table_name)
    cursor.execute(query)
    return cursor
