from flask import request
from flask_restx import Resource, Namespace

from app.container import movie_service
from app.dao.model.movie import MovieSchema

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        did = request.args.get('director_id')
        gid = request.args.get('genre_id')
        year = request.args.get('year')

        all_movies = movie_service.get(did=did, gid=gid, year=year)
        return movies_schema.dump(all_movies), 200

    def post(self):
        data = request.json
        new_movie = movie_service.create(data)
        return '', 201, {'location': f'{movie_ns.path}/{new_movie.id}'}  # Заголовок Location


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get(mid=mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        data_movie = request.json
        return movie_service.update(mid, data_movie), 201

    def patch(self, mid):
        data_movie = request.json
        return movie_service.update_partial(mid, data_movie), 201

    def delete(self, mid):
        return movie_service.delete(mid), 204
