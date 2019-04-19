import aiohttp_jinja2
from aiohttp import web
from aiohttp_security import authorized_userid, remember, check_authorized, forget
from backend.security.db_auth import check_credentials
from db.exceptions import DatabaseException
from passlib.hash import sha256_crypt
from db import db


class LoginRouter:

    async def index(self, request):
        username = await authorized_userid(request)
        if username:
            response = web.HTTPFound('/')
        else:
            context = {'title': 'Login Page'}
            if 'invalid' in request.rel_url.query:
                context.update({'flush': 'Invalid credentials'})
            response = aiohttp_jinja2.render_template('pages/auth/login.html', request, context)
        return response

    async def login(self, request):
        form = await request.post()
        login = form.get('email')
        password = form.get('password')
        login_type = form.get('type')
        db_engine = request.app['db']
        if login_type == 'employer':
            redirect_url = '/employer'
        elif login_type == 'company':
            redirect_url = '/company'
        else:
            redirect_url = '/'
        response = web.HTTPFound(redirect_url)
        if await check_credentials(db_engine, login, password, login_type):
            await remember(request, response, login)
            raise response

        raise web.HTTPFound('/login?invalid=true')

    async def sign_up(self, request):
        username = await authorized_userid(request)
        if username:
            response = web.HTTPFound('/')
        else:
            context = {'title': 'Login Page'}
            if 'message' in request.rel_url.query:
                context.update({'flush': request.rel_url.query['message']})
            response = aiohttp_jinja2.render_template('pages/auth/register.html', request, context)
        return response

    async def register(self, request):
        response = web.HTTPFound('/login')
        form = await request.post()
        reg_type = form.get('type')
        try:
            if reg_type == 'employer':
                d = {'email': form.get('email'),
                     'pass_hash': sha256_crypt.hash(form.get('password')),
                     'first_name': form.get('first_name'),
                     'last_name': form.get('last_name'),
                     'phone': form.get('phone'),
                     }
                async with request.app['db'].acquire() as conn:
                    print(d)
                    res = await db.create_employer(conn, d)
                    print(res)
            elif reg_type == 'company':
                d = {'email': form.get('email'),
                     'pass_hash': sha256_crypt.hash(form.get('password')),
                     'name': form.get('name')
                     }
                async with request.app['db'].acquire() as conn:
                    print(d)
                    res = await db.create_company(conn, d)
                    print(res)
        except DatabaseException:
            response = web.HTTPFound('/register?message=This+user+already+exists')

        raise response

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
        router.add_route('GET', '/register', self.sign_up, name='register')
        router.add_route('POST', '/register', self.register, name='register')
        # router.add_route('GET', '/protected', self.protected_page,
        #                  name='protected')
