import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries

def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

def main():
    # read data warehouse credentials
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    # create connection
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    # create tables
    drop_tables(cur, conn)
    create_tables(cur, conn)

    # close connection
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()