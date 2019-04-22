import aiohttp_jinja2
from aiohttp import web
from aiohttp_security import check_permission, permits, remember, authorized_userid
from backend.security.db_auth import check_credentials
from db import db
from db.exceptions import DatabaseException


class AdminRouter:

    async def index(self, request):
        permission = await permits(request, 'admin')
        if permission:
            response = web.HTTPFound('/admin/page')
        else:
            context = {}
            if 'message' in request.rel_url.query:
                context = {'flush': request.rel_url.query['message']}
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
        response = web.HTTPFound('/admin?message=Invalid+credentials')
        raise response

    async def admin_page(self, request):
        await check_permission(request, 'admin')
        admin = await authorized_userid(request)
        categories = []
        async with request.app['db'].acquire() as conn:
            db_categories = await db.get_categories(conn)
            print(db_categories)
            for category in db_categories:
                categories.append(
                    {'id': category[0],
                     'name': category[1]}
                )

        context = {}

        if 'message' in request.rel_url.query:
            context = {'flush': request.rel_url.query['message']}

        context.update({
            'admin': admin,
            'message': 'this is admin page',
            'categories': categories
        })
        print(context)
        response = aiohttp_jinja2.render_template('pages/admin/admin.html', request, context)
        return response

    async def create_news(self, request):
        await check_permission(request, 'admin')
        form = await request.post()
        news = {
            'title': form.get('title'),
            'text': form.get('text'),
            'date': form.get('date'),
            'image_url': form.get('image_url'),
            'category_fk': form.get('category')
        }
        try:
            async with request.app['db'].acquire() as conn:
                await db.create_news(conn, news)
                return web.HTTPFound('/admin/page?message=News+created')
        except DatabaseException:
            return web.HTTPFound('/admin/page?message=News+was+not+created')

    async def create_category(self, request):
        await check_permission(request, 'admin')
        form = await request.post()
        category = {
            'name': form.get('name'),
            'description': form.get('description'),
            'image_url': form.get('image_url'),
        }
        try:
            async with request.app['db'].acquire() as conn:
                await db.create_category(conn, category)
                return web.HTTPFound('/admin/page?message=Category+created')
        except DatabaseException:
            return web.HTTPFound('/admin/page?message=Category+was+not+created')

    def configure(self, app):
        router = app.router

        router.add_route('GET', '/admin', self.index, name='admin')
        router.add_route('POST', '/admin', self.admin_check, name='admin')
        router.add_route('GET', '/admin/page', self.admin_page, name='admin_page')
        router.add_route('POST', '/news/create', self.create_news, name='create_news')
        router.add_route('POST', '/category/create', self.create_category, name='create_category')
