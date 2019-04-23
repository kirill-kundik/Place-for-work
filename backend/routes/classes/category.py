import aiohttp_jinja2
from aiohttp import web
from aiohttp_security import authorized_userid, permits
from db import db
from db.exceptions import DatabaseException


class CategoryRouter:

    @aiohttp_jinja2.template('pages/category/category.html')
    async def index(self, request):
        async with request.app['db'].acquire() as conn:
            categories = []
            username = await authorized_userid(request)
            if username:
                is_employer = await permits(request, 'employer')
                res_categories = await db.get_categories(conn)
                for category in res_categories:
                    categories.append(
                        {'id': category[0],
                         'name': category[1],
                         'description': category[3][:150] + '...',
                         'image_url': category[2]}
                    )
                return {'title': 'Categories',
                        'username': username,
                        'profile_link': ('employer' if is_employer else 'company'),
                        'categories': categories}
            # cursor = await conn.execute(db.question.select())
            # records = await cursor.fetchall()
            # questions = [dict(q) for q in records]
            res_categories = await db.get_categories(conn)
            for category in res_categories:
                categories.append(
                    {'id': category[0],
                     'name': category[1],
                     'description': category[3][:150] + '...',
                     'image_url': category[2]}
                )
            return {'title': 'Categories',
                    'categories': categories}

    @aiohttp_jinja2.template('pages/category/one_category.html')
    async def one_category(self, request):
        category_id = request.match_info['id']
        try:
            async with request.app['db'].acquire() as conn:
                username = await authorized_userid(request)
                related_news = []

                if username:
                    is_employer = await permits(request, 'employer')
                    res_cat = await db.get_category_by_id(conn, category_id)
                    rel_news = await db.get_news_by_category(conn, res_cat['id'], 0)
                    rel_vac = await db.get_vacancies_by_cat_id(conn, res_cat['id'], 4)
                    related_vac = []
                    for vac in rel_vac:
                        related_vac.append(
                            {
                                'position': vac[1],
                                'description': vac[2],
                                'company_id': vac[6],
                                'company_name': vac[5],
                                'id': vac[0]
                            }
                        )

                    for new in rel_news:
                        related_news.append(
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
                            'category': res_cat,
                            'related_news': related_news,
                            'vacancies': related_vac}

                res_cat = await db.get_category_by_id(conn, category_id)
                rel_news = await db.get_news_by_category(conn, res_cat['id'], 0)
                rel_vac = await db.get_vacancies_by_cat_id(conn, res_cat['id'], 4)
                related_vac = []
                for vac in rel_vac:
                    related_vac.append(
                        {
                            'position': vac[1],
                            'description': vac[2],
                            'company_id': vac[6],
                            'company_name': vac[5],
                            'id': vac[0]
                        }
                    )
                for new in rel_news:
                    related_news.append(
                        {'id': new[0],
                         'title': new[1],
                         'text': new[2][:150] + '...',
                         'date': new[3],
                         'views': new[4],
                         'image_url': new[5]}
                    )
                return {'title': 'News',
                        'category': res_cat,
                        'related_news': related_news,
                        'vacancies': related_vac}
        except DatabaseException:
            raise web.HTTPNotFound()

    def configure(self, app):
        router = app.router

        router.add_route('GET', '/category', self.index, name='category')
        router.add_route('GET', '/category/{id}', self.one_category, name='one_category')
