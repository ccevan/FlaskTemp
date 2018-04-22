# from app import app
from app import Create_app
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager

app, db = Create_app('SonConfig')
manager = Manager(app)
Migrate(app,db)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    print(app.url_map)
    manager.run()