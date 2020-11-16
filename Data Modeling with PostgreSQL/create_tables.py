import psycopg2
import os
from dotenv import load_dotenv
from sql_queries import create_table_queries, drop_table_queries

if(not load_dotenv()):
    raise Exception("Could not read .env file")
else:
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    DB_USERNAME = os.getenv("DB_USERNAME")
    DB_PASSWORD = os.getenv("DB_PASSWORD")

    for k, v in {'DB_HOST': DB_HOST, 'DB_NAME': DB_NAME, 'DB_USERNAME': DB_USERNAME, 'DB_PASSWORD': DB_PASSWORD}.items():
        if(v is None):
            raise Exception(f"Could not find environment variable '{k}'")
        else:
            print(f"Environment variable {k} loaded")

def create_database():
    # connect to postgres server
    conn = psycopg2.connect(f"host=127.0.0.1 user={DB_USERNAME} password={DB_PASSWORD}")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute(f"DROP DATABASE IF EXISTS {DB_NAME}")
    cur.execute(f"CREATE DATABASE {DB_NAME} WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect(f"host=127.0.0.1 dbname={DB_NAME} user={DB_USERNAME} password={DB_PASSWORD}")
    cur = conn.cursor()
    
    return cur, conn

def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()