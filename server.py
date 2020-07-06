from flask import Flask, render_template
from flask_restful import reqparse, Api, Resource

app = Flask(__name__)
app.config.from_object('config')
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('input_vacancy_text', type=str, help='Vacancy text')


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')


class NeuralResult(Resource):
    def post(self):
        args = parser.parse_args()
        print(args)
        #принимаем строку - возвращаем её длину
        #как победить кодировку?
        return {args['input_vacancy_text']: len(args['input_vacancy_text'])}, 200


api.add_resource(NeuralResult, '/')

if __name__ == '__main__':
    app.run()
