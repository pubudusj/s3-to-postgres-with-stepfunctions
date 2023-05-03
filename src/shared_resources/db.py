from sqlalchemy import create_engine
import boto3
import os

ssm_client = boto3.client('ssm')


def get_db_params():
    print(os.environ['DB_CONNECTION_STRING'])
    response = ssm_client.get_parameter(
        Name='/' + os.environ['DB_CONNECTION_STRING'],
        WithDecryption=True
    )

    return response['Parameter']['Value']


def create_db_connection():
    connection_string = get_db_params()

    return create_engine(connection_string)


def get_queries_for_table(table_name):
    if table_name == 'year_2021':
        return {
            'drop': 'DROP TABLE IF EXISTS "dataimport"."year_2021"',
            'create': '''
                    CREATE TABLE "dataimport"."year_2021" (
                      "station_id" text COLLATE "pg_catalog"."default",
                      "date" text COLLATE "pg_catalog"."default",
                      "lat" text COLLATE "pg_catalog"."default",
                      "lng" text COLLATE "pg_catalog"."default",
                      "elevation" text COLLATE "pg_catalog"."default",
                      "name" text COLLATE "pg_catalog"."default",
                      "temp" text COLLATE "pg_catalog"."default",
                      "temp_attributes" text COLLATE "pg_catalog"."default",
                      "dewp" text COLLATE "pg_catalog"."default",
                      "dewp_attributes" text COLLATE "pg_catalog"."default",
                      "slp" text COLLATE "pg_catalog"."default",
                      "slp_attributes" text COLLATE "pg_catalog"."default",
                      "stp" text COLLATE "pg_catalog"."default",
                      "stp_attributes" text COLLATE "pg_catalog"."default",
                      "visib" text COLLATE "pg_catalog"."default",
                      "visib_attributes" text COLLATE "pg_catalog"."default",
                      "wdsp" text COLLATE "pg_catalog"."default",
                      "wdsp_attributes" text COLLATE "pg_catalog"."default",
                      "mxspd" text COLLATE "pg_catalog"."default",
                      "gust" text COLLATE "pg_catalog"."default",
                      "max" text COLLATE "pg_catalog"."default",
                      "max_attributes" text COLLATE "pg_catalog"."default",
                      "min" text COLLATE "pg_catalog"."default",
                      "min_attributes" text COLLATE "pg_catalog"."default",
                      "prcp" text COLLATE "pg_catalog"."default",
                      "prcp_attributes" text COLLATE "pg_catalog"."default",
                      "sndp" text COLLATE "pg_catalog"."default",
                      "frshtt" text COLLATE "pg_catalog"."default"
                    )''',
            'constraints': [],
            'indexes': [],
            'stats': [],
        }
    elif table_name == 'year_2022':
        return {
            'drop': 'DROP TABLE IF EXISTS "dataimport"."year_2022"',
            'create': '''
                    CREATE TABLE "dataimport"."year_2022" (
                      "station_id" text COLLATE "pg_catalog"."default",
                      "date" text COLLATE "pg_catalog"."default",
                      "lat" text COLLATE "pg_catalog"."default",
                      "lng" text COLLATE "pg_catalog"."default",
                      "elevation" text COLLATE "pg_catalog"."default",
                      "name" text COLLATE "pg_catalog"."default",
                      "temp" text COLLATE "pg_catalog"."default",
                      "temp_attributes" text COLLATE "pg_catalog"."default",
                      "dewp" text COLLATE "pg_catalog"."default",
                      "dewp_attributes" text COLLATE "pg_catalog"."default",
                      "slp" text COLLATE "pg_catalog"."default",
                      "slp_attributes" text COLLATE "pg_catalog"."default",
                      "stp" text COLLATE "pg_catalog"."default",
                      "stp_attributes" text COLLATE "pg_catalog"."default",
                      "visib" text COLLATE "pg_catalog"."default",
                      "visib_attributes" text COLLATE "pg_catalog"."default",
                      "wdsp" text COLLATE "pg_catalog"."default",
                      "wdsp_attributes" text COLLATE "pg_catalog"."default",
                      "mxspd" text COLLATE "pg_catalog"."default",
                      "gust" text COLLATE "pg_catalog"."default",
                      "max" text COLLATE "pg_catalog"."default",
                      "max_attributes" text COLLATE "pg_catalog"."default",
                      "min" text COLLATE "pg_catalog"."default",
                      "min_attributes" text COLLATE "pg_catalog"."default",
                      "prcp" text COLLATE "pg_catalog"."default",
                      "prcp_attributes" text COLLATE "pg_catalog"."default",
                      "sndp" text COLLATE "pg_catalog"."default",
                      "frshtt" text COLLATE "pg_catalog"."default"
                    )''',
            'constraints': [],
            'indexes': [],
            'stats': [],
        }
    else:
        return None
