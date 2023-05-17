from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorites = db.relationship('Favorites',backref='owner') 
    
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Characters(db.Model):
    __tablename__='characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    age = db.Column(db.Integer,nullable=False) 
    height = db.Column(db.String(250),nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)

class Planets(db.Model):
    __tablename__='planets'
    id = db.Column(db.Integer,primary_key=True)
    name =  db.Column(db.String(60),nullable=False) 
    description = db.Column(db.String(250), nullable=False)  

class Favorites(db.Model):
    __tablename__='favorites'
    id = db.Column(db.Integer,primary_key=True)
    favorites_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable = False)
    favorites_character_id = db.Column(db.Integer, db.ForeignKey('characters.id')) 
    favorites_planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))

    