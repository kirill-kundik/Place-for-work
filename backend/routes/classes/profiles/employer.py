import aiohttp_jinja2
from aiohttp import web
from aiohttp_security import check_permission, authorized_userid

from db import db


class EmployerRouter:

    async def index(self, request):
        await check_permission(request, 'employer')
        username = await authorized_userid(request)
        context = {
            'username': username,
            'title': 'Profile page',
            'profile_link': 'employer',
            'employer': True,
        }

        async with request.app['db'].acquire() as conn:
            res = await db.get_employer(conn, username)
            context.update(res)

            res = await db.get_employer_resumes(conn, res['id'])
            resumes = []
            for r in res:
                resumes.append({
                    'id': r[0],
                    'perks': r[1],
                    'hobbies': r[2],
                    'category_id': r[3],
                    'category_name': r[4]
                })

            context.update({
                'resumes': resumes
            })

        response = aiohttp_jinja2.render_template('pages/profiles/employer.html', request, context)
        return response

    async def update_employer(self, request):
        await check_permission(request, 'employer')
        username = await authorized_userid(request)
        form = await request.post()
        print(form)

        image_url = form.get('image_url')
        tg_link = form.get('tg_link')
        fb_link = form.get('fb_link')
        skype_link = form.get('skype_link')
        city = form.get('city')
        date_of_birth = form.get('date_of_birth')

        employer_update = {
            'first_name': form.get('first_name'),
            'last_name': form.get('last_name'),
            'phone': form.get('phone'),

            'image_url': (image_url if image_url != '' else None),
            'tg_link': (tg_link if tg_link != '' else None),
            'fb_link': (fb_link if fb_link != '' else None),
            'skype_link': (skype_link if skype_link != '' else None),
            'city': (city if city != '' else None),
            'date_of_birth': (date_of_birth if date_of_birth != '' else None),
        }

        async with request.app['db'].acquire() as conn:
            await db.update_employer(conn, employer_update, username)

        return web.HTTPFound('/employer')

    def configure(self, app):
        router = app.router

        router.add_route('GET', '/employer', self.index, name='employer')
        router.add_route('POST', '/employer', self.update_employer, name='employer')
