import db


def lambda_handler(event, context):
    engine = db.create_db_connection()

    table_name = event['table']
    print("Preparing table {table}".format(table=table_name))
    queries = db.get_queries_for_table(table_name)

    if queries is None:
        raise Exception("Table structure not found for {table}".format(table=table_name))

    with engine.connect() as con:
        with con.begin():
            con.execute(queries['drop'])

        with con.begin():
            con.execute(queries['create'])

        con.close()
