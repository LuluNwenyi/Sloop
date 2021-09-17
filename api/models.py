from api import db

# USER TABLE
class User(db.Model):

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key = True)
    public_id = db.Column(db.String(24), unique = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128))
    admin = db.Column(db.Boolean, default=False)


    def __init__(self, email, username, password, admin, public_id):
        self.email = email
        self.username = username
        self.admin = admin
        self.password = password
        self.public_id = public_id

    db.create_all()