import json
from elasticsearch import Elasticsearch
from apscheduler.schedulers.background import BackgroundScheduler

# get_movie() 함수 정의 (예시로 사용)
def get_movie():
    # 실제 영화 데이터를 반환하는 로직을 작성
    # 여기서는 예시로 하드코딩된 JSON 문자열을 반환
    return '''
    [
        {"title": "Movie 1", "year": 2021, "genre": "Action"},
        {"title": "Movie 2", "year": 2020, "genre": "Drama"}
    ]
    '''

def send_to_elasticsearch():
    # Elasticsearch 클라이언트 생성
    es = Elasticsearch("http://localhost:9200")

    # 인덱스 생성
    index_name = "movie"

    # get_movie() 함수에서 반환된 JSON 데이터를 파싱
    try:
        movie_data = json.loads(get_movie())  # JSON 데이터 불러오기
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return

    # 각 영화 항목을 별도의 문서로 인덱싱
    for movie in movie_data:
        try:
            # es.index() 메서드를 사용하여 데이터를 엘라스틱서치에 저장
            response = es.index(index=index_name, body=movie)
            print(f"Document indexed: {response}")
        except Exception as e:
            print(f"Error indexing document: {e}")

    print("Data sent to Elasticsearch")

# 스케줄러 설정
scheduler = BackgroundScheduler()

# 매 분마다 실행
scheduler.add_job(func=send_to_elasticsearch, trigger="cron", minute="*/1", id="get_movie")

# 스케줄러 시작
scheduler.start()

# 프로그램이 종료되지 않도록 대기 (예: 서버 실행 유지)
try:
    while True:
        pass
except (KeyboardInterrupt, SystemExit):
    # 스케줄러 종료
    scheduler.shutdown()
