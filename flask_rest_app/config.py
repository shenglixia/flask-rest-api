class Development(object):
    DEBUG = True

    ## DB URL FOR DEVELOPMENT
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'


class Testing(object):
    DEBUG = False
    
    ## DB URL FOR TESTING
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'


class Production(object):
    DEBUG = False

    ## DB URL FOR PRODUCTION
    SQLALCHEMY_DATABASE_URI = 'sqlite:///prod.db'
