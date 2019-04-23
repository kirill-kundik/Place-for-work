import aiohttp_jinja2
from aiohttp import web
from aiohttp_security import check_permission, authorized_userid

from db import db
from db.exceptions import DatabaseException


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
            try:
                res = await db.get_status_name(conn, res['status_fk'])
                print('HERE')
                print(res['name'])
                context.update({
                    'status_name': res['name']
                })
            except DatabaseException as e:
                print(e)

            res = await db.get_statuses(conn)
            statuses = [{'id': r[0], 'name': r[1]} for r in res]

            context.update({
                'statuses': statuses
            })

        response = aiohttp_jinja2.render_template('pages/profiles/company.html', request, context)
        return response

    async def update_company(self, request):
        await check_permission(request, 'company')
        username = await authorized_userid(request)
        form = await request.post()

        description = form.get('description'),

        image_url = form.get('image_url'),
        employers_cnt = form.get('employers_cnt'),
        est_year = form.get('est_year'),
        site_url = form.get('site_url'),
        main_category = form.get('main_category'),

        company_dict = {
            'name': form.get('name'),
            'description': (description if description != '' else None),

            'image_url': (image_url if image_url != '' else None),
            'employers_cnt': (employers_cnt if employers_cnt != '' else None),
            'est_year': (est_year if est_year != '' else None),
            'site_url': (site_url if site_url != '' else None),
            'main_category': (main_category if main_category != '' else None),
            'status_fk': form.get('status'),
        }

        async with request.app['db'].acquire() as conn:
            await db.update_company(conn, company_dict, username)

        return web.HTTPFound('/company')

    def configure(self, app):
        router = app.router

        router.add_route('GET', '/company', self.index, name='company')
        router.add_route('POST', '/company', self.update_company, name='company')
