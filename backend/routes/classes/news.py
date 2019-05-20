import aiohttp_jinja2
from aiohttp import web
from aiohttp_security import authorized_userid, permits

from db import db
from db.exceptions import DatabaseException


class NewsRouter:

    @aiohttp_jinja2.template('pages/news/news.html')
    async def index(self, request):
        async with request.app['db'].acquire() as conn:
            news = []
            username = await authorized_userid(request)
            if username:
                is_employer = await permits(request, 'employer')
                res_news = await db.get_news(conn)
                for new in res_news:
                    news.append(
                        {'id': new[0],
                         'title': new[1],
                         'text': new[2][:150] + '...',
                         'date': new[3],
                         'views': new[4],
                         'image_url': new[5]}
                    )
                return {'title': 'News',
                        'username': username,
                        'profile_link': ('employer' if is_employer else 'company'),
                        'news': news}
            # cursor = await conn.execute(db.question.select())
            # records = await cursor.fetchall()
            # questions = [dict(q) for q in records]
            res_news = await db.get_news(conn)
            for new in res_news:
                news.append(
                    {'id': new[0],
                     'title': new[1],
                     'text': new[2][:150] + '...',
                     'date': new[3],
                     'views': new[4],
                     'image_url': new[5]}
                )
            return {'title': 'News',
                    'news': news}

    @aiohttp_jinja2.template('pages/news/one_news.html')
    async def one_news(self, request):
        news_id = request.match_info['id']
        try:
            async with request.app['db'].acquire() as conn:
                username = await authorized_userid(request)
                related_news = []

                if username:
                    is_employer = await permits(request, 'employer')
                    res_news = await db.get_news_by_id(conn, news_id)
                    rel_news = await db.get_news_by_category(conn, res_news['category_fk'], res_news['id'])
                    for new in rel_news:
                        related_news.append(
                            {'id': new[0],
                             'title': new[1],
                             'text': new[2][:150] + '...',
                             'date': new[3],
                             'views': new[4],
                             'image_url': new[5]}
                        )
                    return {'title': res_news['title'],
                            'username': username,
                            'profile_link': ('employer' if is_employer else 'company'),
                            'news': res_news,
                            'related_news': related_news}

                res_news = await db.get_news_by_id(conn, news_id)
                rel_news = await db.get_news_by_category(conn, res_news['category_fk'], res_news['id'])
                for new in rel_news:
                    related_news.append(
                        {'id': new[0],
                         'title': new[1],
                         'text': new[2][:150] + '...',
                         'date': new[3],
                         'views': new[4],
                         'image_url': new[5]}
                    )
                return {'title': res_news['title'],
                        'news': res_news,
                        'related_news': related_news}
        except DatabaseException:
            raise web.HTTPNotFound()

    def configure(self, app):
        router = app.router

        router.add_route('GET', '/news', self.index, name='news')
        router.add_route('GET', '/news/{id}', self.one_news, name='one_news')
