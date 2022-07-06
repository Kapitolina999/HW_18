from flask import request, jsonify
from flask_restx import Resource, Namespace

from app.container import genre_service
from app.dao.model.genre import GenreSchema

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genre = genre_service.get()
        return genres_schema.dump(all_genre), 200

    def post(self):
        new_genre = request.json
        genre_service.create(new_genre)
        return '', 201


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre = genre_service.get(gid)
        return genre_schema.dump(genre), 200

    def put(self, gid):
        data_genre = request.json
        data_genre['id'] = gid
        genre_service.update(data_genre)
        return '', 201

    def delete(self, gid):
        genre_service.delete(gid)
        return '', 204
