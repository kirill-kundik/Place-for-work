import aiohttp_jinja2
from aiohttp_security import check_permission, authorized_userid
from db import db


class EmployerRouter:

    async def index(self, request):
        await check_permission(request, 'employer')
        username = await authorized_userid(request)
        context = {
            'username': username,
            'title': 'Profile page',
            'profile_link': 'employer'
        }

        async with request.app['db'].acquire() as conn:
            res = await db.get_employer(conn, username)
            context.update(res)

        response = aiohttp_jinja2.render_template('pages/profiles/employer.html', request, context)
        return response

    async def update_emploter(self, request):
        pass

    def configure(self, app):
        router = app.router

        router.add_route('GET', '/employer', self.index, name='employer')
        router.add_route('POST', '/employer', self.update_emploter, name='employer')
