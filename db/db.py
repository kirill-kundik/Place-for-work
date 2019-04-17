import aiopg.sa
from db import models
from db.exceptions import DuplicateRecordException

__all__ = models.__all__


async def init_pg(app):
    conf = app['config']['postgres']
    engine = await aiopg.sa.create_engine(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port'],
        minsize=conf['minsize'],
        maxsize=conf['maxsize'],
    )
    app['db'] = engine


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()


async def create_employer(conn, employer_dict):
    check = await conn.execute(
        models.employer.select().where(models.employer.c.email == employer_dict['email'])
    )
    res = await check.first()
    if not res:
        employer_dict.update({
            'image_url': None,
            'tg_link': None,
            'fb_link': None,
            'skype_link': None,
            'city': None,
            'date_of_birth': None
        })
        result = await conn.execute(models.employer.insert(), [employer_dict])
        uid = await result.first()
        return uid
    raise DuplicateRecordException


async def create_company(conn, company_dict):
    check = await conn.execute(
        models.company.select().where(models.company.c.email == company_dict['email'])
    )
    res = await check.first()
    if not res:
        result = await conn.execute(models.company.insert(), [{'email': company_dict['email'],
                                                               'pass_hash': company_dict['pass_hash'], 'name':
                                                                   company_dict['name']
                                                               }])
        uid = await result.first()
        return uid
    raise DuplicateRecordException

# TODO there will be db methods
# async def get_question(conn, question_id):
#     result = await conn.execute(
#         question.select()
#             .where(question.c.id == question_id))
#     question_record = await result.first()
#     if not question_record:
#         msg = "Question with id: {} does not exists"
#         raise RecordNotFound(msg.format(question_id))
#     result = await conn.execute(
#         choice.select()
#             .where(choice.c.question_id == question_id)
#             .order_by(choice.c.id))
#     choice_records = await result.fetchall()
#     return question_record, choice_records
# 
# 
# async def vote(conn, question_id, choice_id):
#     result = await conn.execute(
#         choice.update()
#             .returning(*choice.c)
#             .where(choice.c.question_id == question_id)
#             .where(choice.c.id == choice_id)
#             .values(votes=choice.c.votes + 1))
#     record = await result.fetchone()
#     if not record:
#         msg = "Question with id: {} or choice id: {} does not exists"
#         raise RecordNotFound(msg.format(question_id, choice_id))
