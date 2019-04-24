import aiohttp_jinja2
from aiohttp import web
from aiohttp_security import check_permission, authorized_userid, permits

from db import db
from db.exceptions import DatabaseException


class CompanyRouter:

    @aiohttp_jinja2.template('pages/companies/all_companies.html')
    async def all_companies_view(self, request):
        async with request.app['db'].acquire() as conn:
            res = await db.get_companies(conn)
            companies = []
            for r in res:
                companies.append({
                    'id': r[0],
                    'name': r[3],
                    'description': r[5],
                    'image_url': r[6],
                    'est_year': r[8],
                    'site_url': r[9],
                    'main_category': r[10]
                })
            context = {
                'title': 'Companies',
                'companies': companies
            }

        username = await authorized_userid(request)
        if username:
            is_employer = await permits(request, 'employer')
            context.update({
                'username': username,
                'profile_link': ('employer' if is_employer else 'company'),
                'employer': is_employer,
            })
        return context

    @aiohttp_jinja2.template('pages/companies/one_company.html')
    async def one_company_view(self, request):
        c_id = request.match_info['id']
        context = {}
        async with request.app['db'].acquire() as conn:
            try:
                company = await db.get_company_by_id(conn, c_id)
            except DatabaseException:
                raise web.HTTPNotFound
            context.update(company)
            res = await db.get_vacancies_by_comp_id(conn, c_id, 4)
            vacancies = []

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
        username = await authorized_userid(request)
        if username:
            is_employer = await permits(request, 'employer')
            context.update({
                'username': username,
                'profile_link': ('employer' if is_employer else 'company'),
                'employer': is_employer,
            })
        context.update({'title': company['name'],
                        'vacancies': vacancies})
        return context

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
            company_id = res['id']
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

            res = await db.get_vacancies_by_comp_id(conn, company_id)
            company_vac = []
            for r in res:
                company_vac.append({
                    'position': r[1],
                    'description': r[2],
                    'requirements': r[3],
                    'salary': (r[4] if r[4] is not None else 'не зазначено'),
                    'working_type': r[7],
                    'category_id': r[9],
                    'category_name': r[8],
                    'id': r[0]
                })
            context.update({
                'statuses': statuses,
                'vacancies': company_vac
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
        router.add_route('GET', '/companies/{id}', self.one_company_view, name='one_company')
        router.add_route('GET', '/companies', self.all_companies_view, name='all_companies')
