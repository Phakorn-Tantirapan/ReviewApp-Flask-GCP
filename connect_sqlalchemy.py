import os


def connect_by_sqlalchemy(app):
    PASSWORD = os.environ["DB_PASS"] 
    PUBLIC_IP_ADDRESS = os.environ["DB_PUBLIC"] 
    DBNAME = os.environ["DB_NAME"]
    DBUSER = os.environ["DB_USER"]


    # configuration
    app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
    app.config["SQLALCHEMY_DATABASE_URI"]= f"postgresql+psycopg2://{DBUSER}:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True
    return app

def connect_by_unix(app):
    PASSWORD = os.environ["DB_PASS"] 
    PUBLIC_IP_ADDRESS = os.environ["DB_PUBLIC"] 
    DBNAME = os.environ["DB_NAME"]
    DBUSER = os.environ["DB_USER"]
    INSTANCE_NAME =os.environ["INSTANCE_UNIX_SOCKET"]

    # configuration
    app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
    app.config["SQLALCHEMY_DATABASE_URI"]= f"postgresql+pg8000://{DBUSER}:{PASSWORD}@/{DBNAME}?unix_sock={INSTANCE_NAME}/.s.PGSQL.5432"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True
    return app