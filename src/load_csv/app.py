import os
import db


source_bucket = os.environ['SOURCE_S3_BUCKET']
bucket_region = os.environ['BUCKET_REGION']

def write_into_postgres(engine, table, items):
    with engine.connect() as con:
        with con.begin():
            for item in items:
                if item['Key'].endswith('.csv'):
                    query = "SELECT aws_s3.table_import_from_s3('dataimport.{table}','', '(format csv, header true, " \
                            "delimiter '','', null ''NULL'', escape ''\\'')','{s3bucket}','{filepath}', " \
                            "'{region}')"\
                        .format(table=table, s3bucket=source_bucket, filepath=item['Key'], region=bucket_region)

                    rs = con.execute(query)
                    for row in rs:
                        print(row)

        con.close()


def lambda_handler(event, context):
    engine = db.create_db_connection()

    write_into_postgres(engine, event['BatchInput']['table'], event['Items'])
