from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
from app.models.models import db

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Asdf1205@127.0.0.1:3306/billing'

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()