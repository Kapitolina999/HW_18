from flask import request
from flask_restx import Resource, Namespace

from app.container import director_service
from app.dao.model.director import DirectorSchema

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):

        all_director = director_service.get()
        return directors_schema.dump(all_director), 200

    def post(self):
        new_director = request.json
        director_service.create(new_director)
        return '', 201


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        director = director_service.get(did)
        return director_schema.dump(director), 200

    def put(self, did):
        data_director = request.json
        data_director['id'] = did
        director_service.update(data_director)
        return '', 201

    def delete(self, did):
        director_service.delete(did)
        return '', 204
