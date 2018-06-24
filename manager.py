import datetime
import random

from flask import session
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from info import create_app,db, redis_store
from info import models
from info.models import User

"""
manager的作用只是程序的入口，用来运行程序

"""
# redis_store
app = create_app("development")
manager = Manager(app)
Migrate(app,db)
manager.add_command("mysql",MigrateCommand)
@manager.option('-n', '--name', dest='name')
@manager.option('-p', '--password', dest='password')
def create_super_user(name,password):
    user = User()
    user.nick_name = name
    user.password = password
    user.mobile = name
    user.is_admin = True

    session["user_id"] = user.id
    session["is_admin"] = True
    session["nick_name"] = user.nick_name
    session["mobile"] = user.mobile

    db.session.add(user)
    db.session.commit()


# def add_test_users():
#     users = []
#     now = datetime.datetime.now()
#     for num in range(0, 100):
#         try:
#             user = User()
#             user.nick_name = "%011d" % num    category_id = request.json.get("id")

#             user.mobile = "%011d" % num
#             user.password_hash = "pbkdf2:sha256:50000$SgZPAbEj$a253b9220b7a916e03bf27119d401c48ff4a1c81d7e00644e0aaf6f3a8c55829"
#             user.last_login = now - datetime.timedelta(seconds=random.randint(0, 2678400))
#             users.append(user)
#             print(user.mobile)
#         except Exception as e:
#             print(e)
#     with app.app_context():
#         db.session.add_all(users)
#         db.session.commit()
#     print ('OK')



if __name__ == '__main__':
    print(app.url_map)
    # add_test_users()
    manager.run()