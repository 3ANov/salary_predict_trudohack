from server import db


class NeuralModel(db.Model):
    file_name = db.Column(db.String, primary_key=True)
    file = db.Column(db.LargeBinary)

