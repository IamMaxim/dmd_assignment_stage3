import psycopg2
from psycopg2._psycopg import connection
from psycopg2._psycopg import cursor

connection: connection = None


def init():
    try:
        global connection
        if connection is not None:
            return

        connection = psycopg2.connect(user="dmd1_user",
                                      password="passpass",
                                      host="mywarmplace.tk",
                                      port="18636",
                                      database="dmd1")

        cursor = connection.cursor()
        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to ", record, "\n")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        connection = None
        cursor = None


def close():
    if connection:
        connection.close()
        print("PostgreSQL connection is closed")


def execute(query: str):
    try:
        cur: cursor = connection.cursor()
        cur.execute(query)
        record = cur.fetchall()
        connection.commit()
        cur.close()
        return record
    except psycopg2.errors.InFailedSqlTransaction as e:
        # We are currently if a failed transaction, rollback and retry
        connection.rollback()
        return execute(query)
    except psycopg2.InterfaceError as e:
        # PostgreSQL connection was closed, reopen it and retry
        init()
        return execute(query)


init()
