from . import database

class Users(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    user_id = database.Column(database.String(100), unique=True, nullable=False)
    username = database.Column(database.String(100), unique=True, nullable=False)
    password = database.Column(database.String(255), nullable=False)
    email = database.Column(database.String(255), unique=True, nullable=False)
    phone = database.Column(database.String(20), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f'<User {self.username}>'
