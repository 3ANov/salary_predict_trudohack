from flask import Flask, render_template
from flask_restful import reqparse, Api, Resource
from flask_sqlalchemy import SQLAlchemy

from config import Config


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)


api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('input_vacancy_text', type=str, help='Vacancy text')

#from neural_predict import print_prediction

import re
import sklearn
import pickle

class NeuralModel(db.Model):
    file_name = db.Column(db.String, primary_key=True)
    file = db.Column(db.LargeBinary)


TOKEN_RE = re.compile(r'[\w\d]+')


def tokenize_text_simple_regex(txt, min_token_size=4):
    """ This func tokenize text with TOKEN_RE applied ealier """
    txt = txt.lower()
    all_tokens = TOKEN_RE.findall(txt)
    return [token for token in all_tokens if len(token) >= min_token_size]


loaded_model = pickle.loads(NeuralModel.query.filter_by(file_name='model_one').first().file)

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')


class NeuralResult(Resource):
    def post(self):
        args = parser.parse_args()
        print(args)
        #принимаем строку - возвращаем её длину
        #как победить кодировку?
        return {args['input_vacancy_text']: loaded_model.predict([args['input_vacancy_text']]).tolist()[0]}, 200


api.add_resource(NeuralResult, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
