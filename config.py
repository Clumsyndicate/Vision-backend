import os
class Config:
    '''Common app configurations 
    '''
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class DevelopmentConfig(Config):
    ''' Development app configurations'''

    ENV = 'development'
    TESTING = True
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class ProductionConfig(Config):
    ''' Production app configurations'''

    ENV = 'production'
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
