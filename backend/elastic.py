def index(es, vacancy):
    es.index(index='vacancies', doc_type='vacancy', id=vacancy['id'], body=vacancy)


def search(es, keywords):
    body = {
        "query": {
            "multi_match": {
                "query": keywords,
                "fields": ["position", "description", "requirements"]
            }
        }
    }
    res = es.search(index='vacancies', doc_type='vacancy', body=body)
    return res['hits']['hits']
