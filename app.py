# app.py
from flask import Flask
from data_analysis import gender_data  # data_analysis.py에서 gender_data 함수 가져오기
from flask_cors import CORS  # CORS 임포트

from movie_data import send_to_elasticsearch
from movie_search import get_movie_from_elasticsearch

app = Flask(__name__)

# CORS 설정: 'http://localhost:3000'에서만 접근을 허용
CORS(app, origins="http://localhost:3000")

@app.after_request
def after_request(response):
    # 모든 출처에서 요청을 허용하도록 CORS 헤더 추가
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response

# URL과 함수 연결
app.add_url_rule('/api/gender/<region>', 'gender_data', gender_data, methods=['GET'])
app.add_url_rule('/api/elastic', 'send_to_elasticsearch', send_to_elasticsearch, methods=['GET'])
app.add_url_rule('/api/el_movie', 'get_movie_from_elasticsearch', get_movie_from_elasticsearch, methods=['GET'])
if __name__ == '__main__':
    # 모든 IP에서 접근 가능하도록 0.0.0.0으로 설정
    app.run('0.0.0.0', port=5000, debug=True)
