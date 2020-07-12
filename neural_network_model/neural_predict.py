import os
import pickle
import re

import dill as dill

TOKEN_RE = re.compile(r'[\w\d]+')


def tokenize_text_simple_regex(txt, min_token_size=4):
    """ This func tokenize text with TOKEN_RE applied ealier """
    txt = txt.lower()
    all_tokens = TOKEN_RE.findall(txt)
    return [token for token in all_tokens if len(token) >= min_token_size]


def print_prediction(input):

    loaded_model = dill.load(open('model_new_2.pickle', 'rb'))
    return loaded_model.predict([input])

#print(print_prediction('менеджер среднего звена'))