import psycopg2
from configparser import ConfigParser


def getConfig(filename, section='DATABASE'):
    """ configuration database """
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section
    db = {}
    if section in parser:
        params = parser.items(section)
        dataIds = ["db_connection", "db_host", "db_port", "db_database", "db_username", "db_password"]
        for param in params:
            if(param[0] in dataIds):
                db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db

def create_conn():
        try:
            # DATABASE_URL = "postgresql://postgres:postgres123@103.56.92.76:5439/retailcrm"
            DATABASE_URL = "postgresql://postgres:admin12345@localhost:5432/postgres"
            conn = psycopg2.connect(DATABASE_URL)
            print("Succes")
            return conn
        except (Exception) as e:
            error_message = str(e)
            print(error_message)
            return False

create_conn()