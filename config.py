# holds configuratio for the application
import os
class Config:
    '''
    General configuration parent class
    '''
  
    SECRET_KEY = '1234'
    
    
    
    
   

class ProdConfig(Config):
    '''
    production config child class
    
    Args:
        config:parent config class
    '''
    
    
    uri = os.getenv('DATABASE_URL')
    if uri and uri.startswith('postgres://'):
        uri = uri.replace('postgres://', 'postgresql://', 1)
    SQLALCHEMY_DATABASE_URI = uri

class DevConfig(Config):
    '''
    development config child class
    
    Args:
       config:the parent config class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitchdb'
    
    DEBUG = True
    
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234@localhost/pitch_test'
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}