from app.db import db, BaseModelMixin


class Task(db.Model, BaseModelMixin):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    finished = db.Column(db.Integer)

    def __init__(self, title):
        self.title = title
        self.finished = 0

    def json(self):
        return {"name": self.title, "finished": self.finished}

    @property
    def serialize(self):
        return {
            'title': self.title,
            'finished': self.finished
        }
