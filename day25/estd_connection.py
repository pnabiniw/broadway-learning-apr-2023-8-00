# psycopg2 (Py Connector for Postgres)
# It is the package to connect python with postgres


def estd_connection():
    import psycopg2
    conn = psycopg2.connect(
        database="myinfo",
        user="postgres",
        password="password",
        host="127.0.0.1",
        port=5432
    )
    conn.autocommit = True
    print("Connection established successfully !!")
    cursor = conn.cursor()
    return cursor


# DATAGRIP
