from app.dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get(self, gid=None):
        return self.dao.get(gid)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        gid = data['id']
        genre = self.get(gid)
        genre.name = data['name']

        self.dao.update(genre)

    def delete(self, gid):
        self.dao.delete(gid)
