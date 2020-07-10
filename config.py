class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://testuser:testuser@localhost/trudohack_ml_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False