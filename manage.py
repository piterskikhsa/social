import os
from flask_migrate import Migrate, MigrateCommand

from app import create_app, db
from app.models import User, Role


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    app.run()
