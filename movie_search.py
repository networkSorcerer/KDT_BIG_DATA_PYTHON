import json
from elasticsearch import Elasticsearch as es

# 모든 영화 정보 검색
def get_movie_from_elasticsearch():
    search_body = {
        "query": {
            "match_all": {}
        },
        "size": 30
    }
    response = es.search(index="movie", body=search_body)

    # Elasticsearch 응답 객체에서 필요한 데이터 추출
    hits = response.get("hits", {}).get("hits", []) # 검색 결과 중에서 문서 목록을 가져옴
    result = [{"title": hit["_source"]["title"]} for hit in hits] # 검색 결과에서 영화 제목을 추출하여 리스트로 저장

    # 결과 데이터를 JSON 형식의 문자열로 변환
    response_json = json.dumps(result, ensure_ascii=False, indent=2)
    print("결과 : " + response_json)
    return response_json