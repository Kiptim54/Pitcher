import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kiptim:jerotich@localhost/minutepitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '<Flask WTF Secret Key>'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG=True

config_options = {
    'development':DevConfig,
    'production': ProdConfig
}