from psycopg import connect

def get_db_connection():
    db_host = "aws-0-us-east-1.pooler.supabase.com"
    db_port = 6543
    db_name = "postgres"
    db_user = "postgres.enhjcbmzxzmxhweknakn"
    db_password = "Yisbethh_1572"
    connection = connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    )
    return connection

