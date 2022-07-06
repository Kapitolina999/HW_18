from app.dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get(self, did=None):
        return self.dao.get(did)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        did = data['id']
        director = self.get(did)
        director.name = data['name']

        self.dao.update(director)

    def delete(self, did):
        self.dao.delete(did)

