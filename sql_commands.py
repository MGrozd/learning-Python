import sqlite3
import logging

def sqlite_connection(db_path):
    try:
        connector = sqlite3.connect(db_path)
        return connector
    except Error as e:
        logger.error(e)

def sql_insert(connector, table, table_columns, values):
    cursor = connector.cursor()
    query = ''' INSERT INTO {}({}) VALUES {}
            '''.format(table, table_columns, values)

    cursor.execute(query)
    connector.commit()
    return connector

def sql_update(connector, table, column, value, where, where_value):
    cursor = connector.cursor()
    query = ''' UPDATE {} SET {} = {} WHERE {} = {}
            '''.format(table, cloumn, value, where, where_value)

    cursor.execute(query)
    connector.commit()
    return connector

def sql_select_all(connector, table):
    cursor = connector.cursor()
    query = ''' SELECT * FROM {}'''.format(table)

    rows = cursor.fetchall()

    return rows
