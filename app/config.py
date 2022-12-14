from pymysql.constants import CLIENT

class Config(object):
    SECRET_KEY = '648cf6c687c0039253ce82f264f50ae46dc56f3550ea913f2dd417d20357bdad'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@mysql:3306/ctf?charset=utf8mb4&local_infile=1'
    # rename mysql:port
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://WebPageSqlUser:3c5806f50df69ed06da2fa76bf1730da@mysql:3306/SingalPageWebSql?charset=utf8mb4&local_infile=1'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://WebPageSqlUser:3c5806f50df69ed06da2fa76bf1730da@127.0.0.1:3308/SingalPageWebSql?charset=utf8mb4&local_infile=1'
    SQLALCHEMY_ENGINE_OPTIONS = {"connect_args":{"client_flag": CLIENT.MULTI_STATEMENTS}}
    SQLALCHEMY_POOL_RECYCLE = 30
    SQLALCHEMY_POOL_SIZE = 40