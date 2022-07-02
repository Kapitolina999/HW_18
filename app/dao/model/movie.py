from marshmallow import Schema, fields
from sqlalchemy.orm import relationship

from app.setup_db import db


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    year = db.Column(db.Integer)
    description = db.Column(db.Text)
    trailer = db.Column(db.String(250))
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    genre = relationship('Genre')
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))
    director = relationship('Director')


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    year = fields.Int()
    description = fields.Str()
    trailer = fields.Str()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()
