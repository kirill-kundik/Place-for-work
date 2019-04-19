import aiohttp_jinja2
from aiohttp_security import authorized_userid, permits

from db import db


class IndexRouter:

    @aiohttp_jinja2.template('pages/index.html')
    async def index(self, request):
        async with request.app['db'].acquire() as conn:
            news = []
            username = await authorized_userid(request)
            if username:
                is_employer = await permits(request, 'employer')
                res_news = await db.get_main_news(conn)
                for new in res_news:
                    news.append(
                        {'id': new[0],
                         'title': new[1],
                         'text': new[2][:150] + '...',
                         'date': new[3],
                         'views': new[4],
                         'image_url': new[5]}
                    )
                return {'title': 'Place for Work',
                        'username': username,
                        'profile_link': ('employer' if is_employer else 'company'),
                        'employer': (True if is_employer else False),
                        'news': news}
            # cursor = await conn.execute(db.question.select())
            # records = await cursor.fetchall()
            # questions = [dict(q) for q in records]
            res_news = await db.get_main_news(conn)
            for new in res_news:
                news.append(
                    {'id': new[0],
                     'title': new[1],
                     'text': new[2][:150] + '...',
                     'date': new[3],
                     'views': new[4],
                     'image_url': new[5]}
                )
            return {'title': 'Place for Work',
                    'news': news}

    def configure(self, app):
        router = app.router
        router.add_route('GET', '/', self.index, name='index')
