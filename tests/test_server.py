import requests

x = requests.post('http://0.0.0.0:5000/', data={'input_vacancy_text': 'somevalue'})

print(x.json())
