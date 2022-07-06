from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get(self, mid=None, did=None, gid=None, year=None):
        return self.dao.get(mid, did, gid, year)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        mid = data['id']
        movie = self.get(mid)

        movie.title = data['title']
        movie.year = data['year']
        movie.description = data['description']
        movie.trailer = data['trailer']
        movie.rating = data['rating']
        movie.genre_id = data['genre_id']
        movie.director_id = data['director_id']

        self.dao.update(movie)

    def update_partial(self, data):
        mid = data['id']
        movie = self.get(mid)

        if 'title' in data:
            movie.title = data['title']
        if 'year' in data:
            movie.year = data['year']
        if 'description' in data:
            movie.description = data['description']
        if 'trailer' in data:
            movie.trailer = data['trailer']
        if 'rating' in data:
            movie.rating = data['rating']
        if 'genre_id' in data:
            movie.genre_id = data['genre_id']
        if 'director_id' in data:
            movie.director_id = data['director_id']

        self.dao.update(movie)

    def delete(self, mid):
        self.dao.delete(mid)
