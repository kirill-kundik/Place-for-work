from elasticsearch_async import AsyncElasticsearch


async def index(es, vacancy):
    await es.index(index='vacancies', doc_type='vacancy', id=vacancy['id'], body=vacancy)


async def search(es, keywords):
    body = {
        "query": {
            "multi_match": {
                "query": keywords,
                "fields": ["position", "description", "requirements"]
            }
        }
    }
    res = await es.search(index='vacancies', body=body, sort='_score')
    return res['hits']['hits']


async def init_es(app):
    es = AsyncElasticsearch(hosts='es01')
    es.indices.delete(index='vacancies', ignore=[400, 404]) # if needed to drop previous indexes
    app['es'] = es


async def close_es(app):
    await app['es'].transport.close()
    # await app['es'].transport.wait_closed()
