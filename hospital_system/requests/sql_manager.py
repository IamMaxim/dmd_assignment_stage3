import psycopg2
from psycopg2._psycopg import cursor, connection

connection: connection = None
# connection: connection = None
cursor: cursor = None
# cursor: cursor = None


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

        global cursor
        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print(connection.get_dsn_parameters(), "\n")

        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    # finally:
    #     # closing database connection.
    #     if connection:
    #         cursor.close()
    #         connection.close()
    #         print("PostgreSQL connection is closed")


def execute(query: str):
    cursor.execute(query)
    record = cursor.fetchone()
    return record


init()
