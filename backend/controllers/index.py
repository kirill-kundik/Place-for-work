import aiohttp_jinja2


class IndexRouter:

    @aiohttp_jinja2.template('pages/index.html')
    async def index(self, request):
        async with request.app['db'].acquire() as conn:
            # cursor = await conn.execute(db.question.select())
            # records = await cursor.fetchall()
            # questions = [dict(q) for q in records]
            return {'title': 'Place for Work'}

    def configure(self, app):
        router = app.router
        router.add_route('GET', '/', self.index, name='index')
