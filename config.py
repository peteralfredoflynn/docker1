import os


class BaseConfig(object):
    def __init__(self):
        self.BASEDIR = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                os.pardir
            )
        )

        # Flask built in
        # [http://flask.pocoo.org/docs/1.0/config/]
        self.ENV = 'development'
        self.SECRET_KEY = os.environ.get('SECRET_KEY') or 'top_secret'
        # End Flask built in

        # SQLalchemy
        # [http://flask-sqlalchemy.pocoo.org/2.3/config/]
        self.SQLALCHEMY_RECORD_QUERIES = True
        self.SQLALCHEMY_POOL_SIZE = 12
        self.SQLALCHEMY_POOL_TIMEOUT = 120
        self.SQLALCHEMY_MAX_OVERFLOW = 10
        self.SQLALCHEMY_POOL_RECYCLE = 1800
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
        # End SQLalchemy


    @property
    def SQLALCHEMY_DATABASE_URI(self):
        sql_uri = "mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}?binary_prefix=true"

        return sql_uri.format(
            db=os.environ.get('DB_NAME') or 'docker1_{}'.format(self.ENV),
            user=os.environ.get('DB_USER') or 'root',
            passwd=os.environ.get('DB_PASS') or 'root',
            host=os.environ.get('DB_HOST') or 'root',
            port=os.environ.get('DB_PORT') or 3306
        )
