# holds configuratio for the application
import os
class Config:
    '''
    General configuration parent class
    '''
  
    SECRET_KEY = '1234'
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234@localhost/pitch'
    
    
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

class ProdConfig(Config):
    '''
    production config child class
    
    Args:
        config:parent config class
    '''
    
    
    SECRET_KEY = '1234'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234@localhost/pitch'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    DEBUG = True

class DevConfig(Config):
    '''
    development config child class
    
    Args:
       config:the parent config class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234@localhost/pitch'
    DEBUG = True
    
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234@localhost/pitch_test'
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}