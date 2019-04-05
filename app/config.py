import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.getenv('SECRET_KEY', 'ngle_api_tongchun')
	DEBUG = False


class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	ENV = 'development'


class TestingConfig(Config):
	DEBUG = True
	TESTING = True
	PRESERVE_CONTEXT_ON_EXCEPTION = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	ENV = 'testing'


class ProductionConfig(Config):
	DEBUG = False
	ENV = 'production'


config_by_name = dict(
	dev=DevelopmentConfig,
	test=TestingConfig,
	prod=ProductionConfig
)

key = Config.SECRET_KEY