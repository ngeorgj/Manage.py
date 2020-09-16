# ====================================================================================================================
# Application Manager                                                                                   Flask Manager
#
#
# Created by Nivaldo Georg Junior                                                                          15/09/2020
# ====================================================================================================================

# Python Native Libraries
import datetime
import os

"""







"""


# ==================================================================================================================== #
#                                                                                                  COMMON FUNCTIONS    #
# ==================================================================================================================== #

def cmd(bash):
    os.system(f'{bash}')


def create_empty_file(name, size):
    cmd(f'fsutil file createnew {name} {size}')

def create_init_file():
    cmd(f'fsutil file createnew __init__.py 8')

def create_file(filename, content):
    create_empty_file(filename, 5000)
    file = os.getcwd() + "\\" + filename
    f = open(file, 'a')
    f.truncate(0)
    f.write(content)
    f.close()


def create_folder(folder_name):
    cmd(f'mkdir {folder_name}')
    print(f"\nFolder {folder_name} created.\n\n")


def change_directory(dir_name):
    os.chdir(dir_name)


username = input("My name is ")
app_name = input("\nApplication name: ")
blueprint_name = input("\nFirst Blueprint Name: ")

# ==================================================================================================================== #
#                                                                                                     MANAGER CLASS    #
# ==================================================================================================================== #

class Manager:

    def __init__(self):
        self.root = ""
        print("\n > Flask Application Manager.\n")
        print("""                        
1. New Project
2. New Blueprint
        """)

    def menu(self):
        option = str(input("Option Number: "))
        if option == '1':
            pass
        elif option == '2':
            self.create_blueprint()

    def create_blueprint(self):
        print("Blueprint Creator\n")
        # name = input('Blueprint Name: ')
        name = blueprint_name
        create_folder(name.lower())
        change_directory('templates')
        create_empty_file('base.html', 8)
        create_folder(f'{name.lower()}')
        change_directory(f'{name.lower()}')
        create_folder('pages')
        create_folder('components')
        change_directory('..')
        change_directory('..')
        change_directory(name)
        create_file(f'{name.lower()}.py', blueprint_file(name))
        create_file(f'routes.py', routes_file(name))
        create_init_file()
        cmd('cls')
        print(f"""\
\nBlueprint Created\n
   Folder : {name.lower()}
   Files  : routes.py & {name.lower()}.py\n
 Go to your main.py and register the blueprint.\n\n""")

    def create_app(self):
        # BASE FILES
        create_file('commit.py', commit_file())
        create_init_file()
        create_folder(app_name.lower())
        change_directory(app_name.lower())
        create_file('models.py', '# Models.py')
        create_file('forms.py', '# Forms.py')
        create_file('main.py', main_file())
        create_file('config.json', config_file())
        create_file("engine.py", "# Here lies the main class of the application.")

        # FOLDERS & STUFF
        create_folder('utils')
        change_directory('utils')
        create_file('database.py', database_file())
        create_file('extensions.py', extensions_file())
        change_directory('..')
        create_folder('templates')
        create_folder('static')
        change_directory('static')
        create_folder('img')
        create_folder('css')
        create_folder('js')
        change_directory('css')
        create_empty_file('custom.css', 1000)
        change_directory('..')
        change_directory('js')
        create_empty_file('custom.js', 1000)
        change_directory('..')
        change_directory('img')
        create_folder('public')
        create_folder('private')
        change_directory('..')
        change_directory('..')

        self.create_blueprint()


# ==================================================================================================================== #
#                                                                                                             FILES    #
# ==================================================================================================================== #

def blueprint_file(name):
    return f"""\
# ---------------------------------------------------------------------------------------------------------------------
# {app_name.title()}, 2020
# Blueprint to {name.title()}
#
# Description:
#  This is the {name} blueprint file.
#
# Created by: {username}
# {datetime.date.today()}
# ---------------------------------------------------------------------------------------------------------------------

# Python External Libraries
from flask import Blueprint

{name.lower()} = Blueprint('{name.title()}', __name__, url_prefix='/{name.title()}')

# Local Imports
from .routes import *"""


def routes_file(name):
    return f"""\
# ---------------------------------------------------------------------------------------------------------------------
# {app_name.title()}, 2020
# Routes to {name.title()}
#
# Description:
#  This is the routes file.
#  Here will be declared the backend to the views.
#
# Created by: {username}
# {datetime.date.today()}
# ---------------------------------------------------------------------------------------------------------------------

# Python External Libraries
from flask import render_template, request, redirect

# Local Imports
from .{name.lower()} import {name.lower()}

# Blueprint Directory :                                                                  root/templates/{name.lower()}                                      
pages = '{name.title()}/pages'

@{name.lower()}.route('/', methods=['GET', 'POST'])
def sample():
    return render_template(f'{{pages}}/index.html')"""

def main_file():
    return f"""\
# ---------------------------------------------------------------------------------------------------------------------
# {app_name.title()}, 2020
# Main
#
# Description:
#  This is the main file.
#  Here will happen flask bindings, blueprint calls and database.
#
# Created by: {username}
# {datetime.date.today()}
# ---------------------------------------------------------------------------------------------------------------------

# Python Native Library Imports
import datetime

# Python External Packages

from {app_name.lower()}.utils.extensions import db
from flask import Flask, render_template, request, redirect, session
from flask_login import LoginManager, current_user

# {app_name.title()} Package Imports

def app_factory(config_filename):
    app = Flask(__name__)
    app.config.from_json("config.json")

    # Database Declaration
    db.init_app(app)
    with app.app_context():
        from {app_name.lower()}.models.user import User
        # Create an User.
        pass

    # Blueprints

    # Flask Login
    login_manager = LoginManager(app)

    return app, db, login_manager

# Application, Database and Login Manager.
app, db, login_manager = app_factory("config.json")


@login_manager.user_loader
def user_loader(user_id):
    from {app_name.lower()}.models.user import User
    return User.query.get(user_id)

@app.route('/')
def landing_page():
    return "Some Cool Landing Page"

if __name__ == "__main__":
    app.run(debug=True)"""

def config_file():
    return f"""\
{{
    "APP_NAME": "{app_name.upper()}",
    "APP_CREATOR": "{username.upper()}",
    "APP_SUBTITLE": "please edit this.",
    "SQLALCHEMY_TRACK_MODIFICATIONS": "False",
    "SQLALCHEMY_DATABASE_URI": "sqlite:///database.db",
    "SECRET_KEY": "###ThisNeedToBeChanged###",
}}"""

def commit_file():
    return f"""\
# ---------------------------------------------------------------------------------------------------------------------
# {app_name}, 2020
# Commit
#
# Description:
#  This script add + commit everything to the main repo.
#  PS. Use this file after configuring a github repository/remote to your machine.
#
# Created by: {username}
# {datetime.date.today()}
# ---------------------------------------------------------------------------------------------------------------------

import os

os.system('clear')
m = input("Message: ")
os.system(f"git add .")
os.system(f'git commit -m "{{m}}"')
os.system("git push -u origin master")"""

def extensions_file():
    return f"""\
# ---------------------------------------------------------------------------------------------------------------------
# {app_name.title()}, 2020
# Extensions
# 
# Description:
# This script serves as reference for some variables like 'db'
# These vars will be initialized in the app_factory @ root/{app_name}/main.py
#
# Created by: {username}
# {datetime.date.today()}
# ---------------------------------------------------------------------------------------------------------------------

# Python External Packages
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()"""

def database_file():
    return f"""\
# ---------------------------------------------------------------------------------------------------------------------
# {app_name}, 2020
# Database
# 
# Description:
#  This file serves as a reference for models. Contains an inheritable class.
#
# Created by: {username}
# {datetime.date.today()}
# ---------------------------------------------------------------------------------------------------------------------

# Folder Imports
from {app_name.lower()}.utils.extensions import db

# Aliases
Column = db.Column
Integer = db.Integer
Float = db.Float
String = db.String
ForeignKey = db.ForeignKey
relationship = db.relationship

class Model(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        db.session.delete(self)
        return commit and db.session.commit()"""


a = Manager()
a.create_app()
a.menu()
