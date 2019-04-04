import os
from .database import db_uri

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.getenv('SECRET_KEY', 'ngle_api_tongchun')
	DEBUG = False


class DevelopmentConfig(Config):
	# uncomment the line below to use postgres
	# SQLALCHEMY_DATABASE_URI = postgres_local_base
	DEBUG = True
	# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_main.db')
	SQLALCHEMY_DATABASE_URI = db_uri
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	ENV = 'development'


class TestingConfig(Config):
	DEBUG = True
	TESTING = True
	# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_test.db')
	SQLALCHEMY_DATABASE_URI = db_uri
	PRESERVE_CONTEXT_ON_EXCEPTION = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	ENV = 'testing'


class ProductionConfig(Config):
	DEBUG = False
	# uncomment the line below to use postgres
	# SQLALCHEMY_DATABASE_URI = postgres_local_base
	ENV = 'production'


config_by_name = dict(
	dev=DevelopmentConfig,
	test=TestingConfig,
	prod=ProductionConfig
)

key = Config.SECRET_KEY