import aiohttp_jinja2
from aiohttp import web
from aiohttp_security import check_permission, authorized_userid
from db import db


class ResumeRouter:
    @aiohttp_jinja2.template('pages/resume/one_resume.html')
    async def index(self, request):
        pass

    async def update(self, request):
        pass

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
        # TODO responses
