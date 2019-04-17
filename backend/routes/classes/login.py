import aiohttp_jinja2
from aiohttp import web
from aiohttp_security import authorized_userid, remember, check_authorized, forget, check_permission
from backend.security.db_auth import check_credentials


class LoginRouter:

    @aiohttp_jinja2.template('pages/login.html')
    async def index(self, request):
        username = await authorized_userid(request)
        if username:
            res = {'message': 'Hey, ' + username}
        else:
            res = {'message': 'You need to login'}
        return res

    async def login(self, request):
        response = web.HTTPFound('/')
        form = await request.post()
        login = form.get('email')
        password = form.get('password')
        login_type = form.get('type')
        db_engine = request.app['db']
        if await check_credentials(db_engine, login, password, login_type):
            await remember(request, response, login)
            raise response

        raise web.HTTPUnauthorized(
            body=b'Invalid username/password combination')

    async def logout(self, request):
        await check_authorized(request)
        response = web.HTTPFound('/')
        await forget(request, response)
        raise response

    # async def protected_page(self, request):
    #     await check_authorized(request)
    #     context = {
    #         'message': 'you are authorized'
    #     }
    #     response = aiohttp_jinja2.render_template('pages/login.html', request, context)
    #     return response

    def configure(self, app):
        router = app.router
        router.add_route('GET', '/login', self.index, name='login')
        router.add_route('POST', '/login', self.login, name='login')
        router.add_route('GET', '/logout', self.logout, name='logout')

        # router.add_route('GET', '/protected', self.protected_page,
        #                  name='protected')
