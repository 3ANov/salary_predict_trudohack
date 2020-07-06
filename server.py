from flask import Flask, render_template
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
app.config.from_object('config')
api = Api(app)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')


class NeuralResult(Resource):
    def post(self):
        return {1: 22}


api.add_resource(NeuralResult, '/')

if __name__ == '__main__':
    app.run()
