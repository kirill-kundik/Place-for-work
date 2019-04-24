import aiohttp_jinja2
from aiohttp_security import authorized_userid, permits
from db import db


class SearchRoute:

    @aiohttp_jinja2.template('pages/search.html')
    async def search(self, request):

        keywords = None
        if 'keywords' in request.rel_url.query:
            keywords = request.rel_url.query['keywords']

        username = await authorized_userid(request)
        context = {}
        if username:
            is_employer = await permits(request, 'employer')
            context = {
                'username': username,
                'profile_link': ('employer' if is_employer else 'company'),
                'employer': is_employer
            }
        vacancies = []
        if keywords:
            async with request.app['db'].acquire() as conn:
                res = await db.get_vacancies(conn)

                for r in res:
                    vacancies.append(
                        {
                            'position': r[1],
                            'description': (r[2][:150] + '...'),
                            'requirements': (r[3][:150] + '...'),
                            'working_type': r[7],
                            'salary': (r[4] if r[4] is not None else 'не зазначено'),
                            'company_id': r[6],
                            'company_name': r[5],
                            'id': r[0],
                            'category_id': r[9],
                            'category_name': r[8]
                        }
                    )

        context.update({
            'title': 'Vacancies',
            'vacancies': vacancies,
            'keywords': keywords
        })
        # print(context)
        return context

    def configure(self, app):
        router = app.router

        router.add_route('GET', '/search', self.search, name='search')
