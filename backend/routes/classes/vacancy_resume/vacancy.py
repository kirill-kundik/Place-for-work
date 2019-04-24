import aiohttp_jinja2
from aiohttp import web
from aiohttp_security import check_permission, authorized_userid, permits

from backend.elastic import index
from db import db


class VacancyRouter:

    @aiohttp_jinja2.template('pages/vacancy/vacancy.html')
    async def index(self, request):
        username = await authorized_userid(request)
        context = {}
        if username:
            is_employer = await permits(request, 'employer')
            context = {
                'username': username,
                'profile_link': ('employer' if is_employer else 'company'),
                'employer': is_employer
            }
        async with request.app['db'].acquire() as conn:
            res = await db.get_vacancies(conn)
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
            context.update({
                'title': 'Vacancies',
                'vacancies': vacancies
            })
        return context

    async def create(self, request):
        await check_permission(request, 'company')
        username = await authorized_userid(request)

        form = await request.post()
        print(form)
        position = form.get('position')
        description = form.get('description')
        requirements = form.get('requirements')
        salary = form.get('salary')

        working_type = form.get('working_type')
        category = form.get('category')

        async with request.app['db'].acquire() as conn:
            v_id = await db.create_vacancy(conn, {
                'position': position,
                'description': description,
                'requirements': requirements,
                'salary': (salary if salary != '' else None),
                'working_type_fk': working_type,
                'category_fk': category
            }, username)
            index(request.app['es'], {
                'id': v_id,
                'position': position,
                'description': description,
                'requirements': requirements
            })
            return web.HTTPFound(f'/vacancy/{v_id[0]}')

    @aiohttp_jinja2.template('pages/vacancy/vacancy_create.html')
    async def create_page(self, request):
        await check_permission(request, 'company')
        username = await authorized_userid(request)
        context = {
            'username': username,
            'title': 'Create vacancy',
            'profile_link': 'company',
            'employer': False
        }
        if 'message' in request.rel_url.query:
            context.update({'flush': request.rel_url.query['message']})
        async with request.app['db'].acquire() as conn:
            context.update({
                'categories': [{'id': cat[0], 'name': cat[1]} for cat in await db.get_categories(conn)],
                'types': [{'id': typ[0], 'name': typ[1]} for typ in await db.get_working_types(conn)]
            })
        return context

    @aiohttp_jinja2.template('pages/vacancy/one_vacancy.html')
    async def one_page(self, request):
        v_id = request.match_info['id']
        username = await authorized_userid(request)
        async with request.app['db'].acquire() as conn:
            vacancy = await db.get_vacancy(conn, v_id)
        if not vacancy:
            raise web.HTTPNotFound
        if username:
            is_employer = await permits(request, 'employer')
            context = {
                'title': '',
                'username': username,
                'profile_link': ('employer' if is_employer else 'company'),
                'employer': (True if is_employer else False),
                'vacancy': vacancy
            }
        else:
            context = {
                'title': '',
                'vacancy': vacancy
            }
        return context

    def configure(self, app):
        router = app.router

        router.add_route('GET', '/vacancy/create', self.create_page, name='create_vacancy')
        router.add_route('POST', '/vacancy/create', self.create, name='create_vacancy')
        router.add_route('GET', '/vacancy/{id}', self.one_page, name='one_vacancy_page')
        router.add_route('GET', '/vacancy', self.index, name='vacancies')
