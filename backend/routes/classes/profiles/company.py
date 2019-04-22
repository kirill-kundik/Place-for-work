import aiohttp_jinja2
from aiohttp import web
from aiohttp_security import check_permission, authorized_userid
from passlib.handlers.sha2_crypt import sha256_crypt

from db import db


class CompanyRouter:

    async def index(self, request):
        await check_permission(request, 'company')
        username = await authorized_userid(request)
        context = {
            'username': username,
            'title': 'Company page',
            'profile_link': 'company',
            'employer': False
        }

        async with request.app['db'].acquire() as conn:
            res = await db.get_company(conn, username)
            context.update(res)

        response = aiohttp_jinja2.render_template('pages/profiles/company.html', request, context)
        return response

    async def update_company(self, request):
        await check_permission(request, 'company')
        username = await authorized_userid(request)
        form = await request.post()

        company_dict = {
            'name': form.get('name'),
            'description': form.get('description'),

            'image_url': form.get('image_url'),
            'employers_cnt': form.get('employers_cnt'),
            'est_year': form.get('est_year'),
            'site_url': form.get('site_url'),
            'main_category': form.get('main_category'),
        }

        async with request.app['db'].acquire() as conn:
            await db.update_company(conn, company_dict, username)

        return web.HTTPFound('/company')

    def configure(self, app):
        router = app.router

        router.add_route('GET', '/company', self.index, name='company')
        router.add_route('POST', '/company', self.update_company, name='company')
