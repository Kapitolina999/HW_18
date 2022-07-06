from app.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    # Вернет все фильмы или фильм по заданному mid
    def get(self, mid=None, did=None, gid=None, year=None):
        if mid:
            return self.session.query(Movie).get(mid)
        if did:
            return self.session.query(Movie).filter(Movie.director_id == did).all()
        if gid:
            return self.session.query(Movie).filter(Movie.genre_id == gid).all()
        if year:
            return self.session.query(Movie).filter(Movie.year == year).all()

        return self.session.query(Movie).all()

    def create(self, data):
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

        return movie

    def delete(self, mid):
        movie = self.get(mid)
        self.session.delete(movie)
        self.session.commit()

