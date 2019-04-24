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
    res = await es.search(index='vacancies', doc_type='vacancy', body=body)
    return res['hits']['hits']


async def init_es(app):
    client = AsyncElasticsearch()
    app['es'] = client


async def close_es(app):
    await app['es'].transport.close()
    # await app['es'].transport.wait_closed()
