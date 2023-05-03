import db


def lambda_handler(event, context):
    engine = db.create_db_connection()

    table_name = event['table']
    print("Preparing table {table}".format(table=table_name))

    with engine.connect() as con:
        print('Starting switching tables')
        with con.begin():
            drop = "DROP TABLE IF EXISTS databackup.{table}".format(table=table_name)
            print(drop)
            con.execute(drop)

        with con.begin():
            rename_table_1 = "ALTER TABLE IF EXISTS public.{table} SET SCHEMA databackup".format(table=table_name)
            print(rename_table_1)
            con.execute(rename_table_1)

            rename_table_2 = "ALTER TABLE dataimport.{table} SET SCHEMA public".format(table=table_name)
            print(rename_table_2)
            con.execute(rename_table_2)

        con.close()
