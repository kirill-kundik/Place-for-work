import aiohttp_jinja2
from aiohttp_security import check_permission, authorized_userid
from db import db


class CompanyRouter:

    async def index(self, request):
        await check_permission(request, 'company')
        username = await authorized_userid(request)
        context = {
            'username': username,
            'title': 'Company page',
            'profile_link': 'company'
        }

        async with request.app['db'].acquire() as conn:
            res = await db.get_company(conn, username)
            context.update(res)

        response = aiohttp_jinja2.render_template('pages/profiles/company.html', request, context)
        return response

    async def update_emploter(self, request):
        pass

    def configure(self, app):
        router = app.router

        router.add_route('GET', '/company', self.index, name='company')
        router.add_route('POST', '/company', self.update_emploter, name='company')
