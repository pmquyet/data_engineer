import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


# drop table if it exist
def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

# create staging, fact and dimension tables
def create_tables(cur, conn): 
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

# connect to database and run above functions
def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)
    print('Table has created')
    conn.close()


if __name__ == "__main__":
    main()