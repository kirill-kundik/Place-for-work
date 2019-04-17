import aiohttp_jinja2
from aiohttp import web
from aiohttp_security import check_permission, permits, remember, authorized_userid
from backend.security.db_auth import check_credentials


class AdminRouter:

    async def index(self, request):
        permission = await permits(request, 'admin')
        if permission:
            response = web.HTTPFound('/admin/page')
        else:
            context = {}
            if 'invalid' in request.rel_url.query:
                context = {'flush': 'Invalid credentials'}
            response = aiohttp_jinja2.render_template('pages/admin/admin.html', request, context)
        return response

    async def admin_check(self, request):
        response = web.HTTPFound('/admin/page')
        form = await request.post()
        login = form.get('email')
        password = form.get('password')
        db_engine = request.app['db']
        if await check_credentials(db_engine, login, password, 'admin'):
            await remember(request, response, login)
            raise response
        response = web.HTTPFound('/admin?invalid=true')
        raise response

    async def admin_page(self, request):
        await check_permission(request, 'admin')
        admin = await authorized_userid(request)
        context = {
            'admin': admin,
            'message': 'this is admin page'
        }
        response = aiohttp_jinja2.render_template('pages/admin/admin.html', request, context)
        return response

    def configure(self, app):
        router = app.router

        router.add_route('GET', '/admin', self.index, name='admin')
        router.add_route('POST', '/admin', self.admin_check, name='admin')
        router.add_route('GET', '/admin/page', self.admin_page, name='admin_page')
