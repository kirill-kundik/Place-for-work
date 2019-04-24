import aiohttp_jinja2
from aiohttp import web
from aiohttp_security import authorized_userid, permits

from backend.elastic import search


class SearchRoute:

    async def test_searh(self, request):
        keywords = request.rel_url.query['q']
        return web.json_response(await search(request.app['es'], keywords))

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
            res = await search(request.app['es'], keywords)
            for r in res:
                r = r['_source']
                vacancies.append({
                    'id': r['id'],
                    'position': r['position'],
                    'description': r['description'],
                    'requirements': r['requirements'],
                    'salary': r['salary'],
                    'category_id': r['category_id'],
                    'category_name': r['category_name'],
                    'working_type': r['working_type'],
                    'company_name': r['company_name'],
                    'company_id': r['company_id'],
                })
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
        router.add_route('GET', '/testSearch', self.test_searh, name='test_search')
