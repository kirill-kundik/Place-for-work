import aiohttp_jinja2
from aiohttp import web
from aiohttp_security import check_permission, authorized_userid, permits
from db import db


class ResumeRouter:
    @aiohttp_jinja2.template('pages/resume/one_resume.html')
    async def index(self, request):
        is_employer = await permits(request, 'employer')
        is_company = await permits(request, 'company')
        if not is_company and not is_employer:
            raise web.HTTPUnauthorized()

        r_id = request.match_info['id']
        username = await authorized_userid(request)
        async with request.app['db'].acquire() as conn:
            if is_employer and await db.check_employer_resume(conn, username, r_id):
                context = {
                    'is_employer': True,
                    'profile_link': 'employer'
                }
            elif is_company and await db.check_company_resume(conn, username, r_id):
                context = {
                    'is_employer': False,
                    'profile_link': 'company',
                }
            else:
                raise web.HTTPUnauthorized()
            resume = await db.get_resume(conn, r_id)
            experiences = []

            res = await db.get_resume_experience(conn, r_id)

            for r in res:
                experiences.append({
                    'title': r[1],
                    'description': r[2],
                    'starting_date': r[3],
                    'ending_date': r[4]
                })

            context.update({
                'experiences': experiences,
                'resume': resume,
                'title': 'Employer Resume',
                'username': username
            })
        return context

    async def update(self, request):
        await check_permission(request, 'employer')
        username = await authorized_userid(request)
        form = await request.post()

        r_id = form.get('resume_id')

        async with request.app['db'].acquire() as conn:
            if not await db.check_employer_resume(conn, username, r_id):
                raise web.HTTPUnauthorized()
            ending_date = form.get('ending_date')
            await db.create_resume_experience(conn, {
                'title': form.get('title'),
                'resume_fk': r_id,
                'description': form.get('description'),
                'starting_date': form.get('starting_date'),
                'ending_date': (ending_date if ending_date != '' else None)
            })
        return web.HTTPFound(f'/resume/{r_id}')

    async def create(self, request):
        await check_permission(request, 'employer')
        username = await authorized_userid(request)

        form = await request.post()
        perks = form.get('perks')
        hobbies = form.get('hobbies')

        category = form.get('category')

        async with request.app['db'].acquire() as conn:
            r_id = await db.create_resume(conn, {
                'perks': perks,
                'hobbies': (hobbies if hobbies != '' else None),
                'category_fk': category
            }, username)
            return web.HTTPFound(f'/resume/{r_id[0]}')

    @aiohttp_jinja2.template('pages/resume/resume_create.html')
    async def create_page(self, request):
        await check_permission(request, 'employer')
        username = await authorized_userid(request)
        context = {
            'username': username,
            'title': 'Create resume',
            'profile_link': 'employer',
            'employer': True
        }
        async with request.app['db'].acquire() as conn:
            context.update({
                'categories': [{'id': cat[0], 'name': cat[1]} for cat in await db.get_categories(conn)]
            })
        return context

    def configure(self, app):
        router = app.router

        router.add_route('GET', '/resume/create', self.create_page, name='create_resume')
        router.add_route('POST', '/resume/create', self.create, name='create_resume')
        router.add_route('POST', '/resume/update', self.update, name='update_resume')
        router.add_route('GET', '/resume/{id}', self.index, name='one_resume')
