from api import db

# USER TABLE
class User(db.Model):

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key = True)
    public_id = db.Column(db.String(24), unique = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    display_name = db.Column(db.String(64))
    password = db.Column(db.String(128))
    admin = db.Column(db.Boolean, default=False)
    creator = db.Column(db.Boolean, default=False)
    website = db.Column(db.String(128))
    bio = db.Column(db.String(140))
    profile_pic = db.Column(db.String(128))


    def __init__(self, email, username, password, admin, public_id, creator, website, bio, profile_pic):
        self.email = email
        self.username = username
        self.admin = admin
        self.password = password
        self.public_id = public_id
        self.creator = creator
        self.website = website
        self.bio = bio
        self.profile_pic = profile_pic


    db.create_all()



# TOKEN TABLE
class TokenBlocklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    db.create_all()