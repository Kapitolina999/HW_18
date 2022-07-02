from flask import request
from flask_restx import Resource, Namespace

from app.container import director_service
from app.dao.model.director import DirectorSchema

director_ns = Namespace('director')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):

        all_director = director_service.get_all()
        return directors_schema.dump(all_director), 200

    def post(self):
        new_director = request.json
        director_service.create(new_director)
        return director_service.create(new_director), 201


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        director = director_service.get_one(did)
        return director_schema.dump(director), 200

    def put(self, did):
        data_director = request.json
        did = data_director['id']
        return director_service.update(data_director), 201

    def delete(self, did):
        return director_service.delete(did), 204
