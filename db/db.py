import aiopg.sa
from db import models
from db.exceptions import *

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
        stmt = models.employer.insert().values(email=employer_dict['email'], pass_hash=employer_dict['pass_hash'],
                                               first_name=employer_dict['first_name'],
                                               last_name=employer_dict['last_name'],
                                               phone=employer_dict['phone'])
        result = await conn.execute(stmt)
        uid = await result.first()
        return uid[0]
    raise DuplicateRecordException


async def create_company(conn, company_dict):
    check = await conn.execute(
        models.company.select().where(models.company.c.email == company_dict['email'])
    )
    res = await check.first()
    if not res:
        stmt = models.company.insert().values(email=company_dict['email'], pass_hash=company_dict['pass_hash'],
                                              name=company_dict['name'])
        result = await conn.execute(stmt)
        uid = await result.first()
        print(uid[0])
        return uid[0]
    raise DuplicateRecordException


async def create_news(conn, news_dict):
    stmt = models.news.insert().values(title=news_dict['title'], text=news_dict['text'], date=news_dict['date'],
                                       image_url=news_dict['image_url'], category_fk=news_dict['category_fk'])
    await conn.execute(stmt)


async def create_category(conn, cat_dict):
    stmt = models.category.insert().values(name=cat_dict['name'], image_url=cat_dict['image_url'],
                                           description=cat_dict['description'])
    await conn.execute(stmt)


async def create_vacancy(conn, vacancy_dict, email):
    stmt = """
    INSERT INTO vacancy(position, description, requirements, salary, working_type_fk, company_fk, category_fk) 
    VALUES ('%s', '%s', '%s', '%s', %s, (SELECT id FROM company WHERE email = '%s'), %s) RETURNING id
    """ % (vacancy_dict['position'], vacancy_dict['description'], vacancy_dict['requirements'], vacancy_dict['salary'],
           vacancy_dict['working_type_fk'], email, vacancy_dict['category_fk'])
    res = await conn.execute(stmt)
    return await res.fetchone()


async def get_categories(conn):
    stmt = models.category.select()
    res = await conn.execute(stmt)
    result = await res.fetchall()
    return result


async def get_category_by_id(conn, cat_id):
    stmt = models.category.select().where(models.category.c.id == cat_id)
    res = await conn.execute(stmt)
    result = await res.fetchone()
    if not result:
        raise RecordNotFound
    return result


async def get_employer(conn, email):
    check = await conn.execute(
        models.employer.select().where(models.employer.c.email == email)
    )
    res = await check.fetchone()
    if not res:
        raise UserDoesNotExistsException
    return res


async def get_main_news(conn):
    stmt = models.news.select().order_by(models.news.c.views.desc()).limit(8)
    res = await conn.execute(stmt)
    result = await res.fetchall()
    return result


async def get_news(conn):
    stmt = models.news.select().order_by(models.news.c.date.desc())
    res = await conn.execute(stmt)
    result = await res.fetchall()
    return result


async def get_news_by_id(conn, news_id):
    result = await conn.execute(
        models.news.update().returning(*models.news.c).where(models.news.c.id == news_id).values(
            views=models.news.c.views + 1)
    )
    record = await result.fetchone()
    if not record:
        raise RecordNotFound
    return record


async def get_news_by_category(conn, cat_id, news_id):
    # print(cat_id, news_id)
    stmt = models.news.select() \
        .where(models.news.c.category_fk == cat_id) \
        .where(models.news.c.id != news_id) \
        .order_by(models.news.c.views.desc()) \
        .limit(4)
    res = await conn.execute(stmt)
    result = await res.fetchall()
    return result


async def get_company(conn, email):
    check = await conn.execute(
        models.company.select().where(models.company.c.email == email)
    )
    res = await check.fetchone()
    if not res:
        raise UserDoesNotExistsException
    return res


async def get_statuses(conn):
    stmt = models.status.select()
    res = await conn.execute(stmt)
    return await res.fetchall()


async def get_working_types(conn):
    stmt = models.working_type.select()
    res = await conn.execute(stmt)
    return await res.fetchall()


async def get_status_name(conn, status_id):
    stmt = models.status.select().where(models.status.c.id == status_id)
    res = await conn.execute(stmt)
    result = await res.fetchone()
    if not result:
        raise RecordNotFound
    return result


async def get_vacancy(conn, v_id):
    stmt = """
    SELECT v.position, v.description, v.requirements, v.salary, c2.name AS company_name, c2.id AS company_id,
    wt.name AS work_type, c.name AS category_name, c.id AS category_id 
    FROM vacancy v 
    INNER JOIN category c on v.category_fk = c.id 
    INNER JOIN company c2 on v.company_fk = c2.id
    INNER JOIN working_type wt on v.working_type_fk = wt.id
    WHERE v.id = %s
    """ % v_id
    res = await conn.execute(stmt)
    return await res.fetchone()


async def get_vacancies_by_cat_id(conn, cat_id, limit=None):
    stmt = """
    SELECT v.id, v.position, v.description, v.requirements, v.salary, c2.name AS company_name, c2.id AS company_id,
    wt.name AS work_type, c.name AS category_name, c.id AS category_id 
    FROM vacancy v 
    INNER JOIN category c on v.category_fk = c.id 
    INNER JOIN company c2 on v.company_fk = c2.id
    INNER JOIN working_type wt on v.working_type_fk = wt.id
    WHERE c.id = %s
    """ % cat_id
    if limit:
        stmt + f" LIMIT {limit}"
    res = await conn.execute(stmt)
    return await res.fetchall()


async def get_vacancies_by_comp_id(conn, comp_id, limit=None):
    stmt = """
    SELECT v.id, v.position, v.description, v.requirements, v.salary, c2.name AS company_name, c2.id AS company_id,
    wt.name AS work_type, c.name AS category_name, c.id AS category_id 
    FROM vacancy v 
    INNER JOIN category c on v.category_fk = c.id 
    INNER JOIN company c2 on v.company_fk = c2.id
    INNER JOIN working_type wt on v.working_type_fk = wt.id
    WHERE c2.id = %s
    """ % comp_id
    if limit:
        stmt + f" LIMIT {limit}"
    res = await conn.execute(stmt)
    return await res.fetchall()


async def get_vacancies(conn, limit=None):
    stmt = """
    SELECT v.id, v.position, v.description, v.requirements, v.salary, c2.name AS company_name, c2.id AS company_id,
    wt.name AS work_type, c.name AS category_name, c.id AS category_id 
    FROM vacancy v 
    INNER JOIN category c on v.category_fk = c.id 
    INNER JOIN company c2 on v.company_fk = c2.id
    INNER JOIN working_type wt on v.working_type_fk = wt.id
    """
    if limit:
        stmt = stmt + f' LIMIT {limit}'
    res = await conn.execute(stmt)
    return await res.fetchall()


async def update_employer(conn, employer_dict, email):
    stmt = models.employer \
        .update() \
        .where(models.employer.c.email == email) \
        .values(first_name=employer_dict['first_name'],
                last_name=employer_dict['last_name'], phone=employer_dict['phone'],
                image_url=employer_dict['image_url'], tg_link=employer_dict['tg_link'],
                fb_link=employer_dict['fb_link'], skype_link=employer_dict['skype_link'], city=employer_dict['city'],
                date_of_birth=employer_dict['date_of_birth'])
    await conn.execute(stmt)


async def update_company(conn, company_dict, email):
    stmt = models.company \
        .update() \
        .where(models.company.c.email == email) \
        .values(name=company_dict['name'],
                description=company_dict['description'],
                image_url=company_dict['image_url'], employers_cnt=company_dict['employers_cnt'],
                est_year=company_dict['est_year'], site_url=company_dict['site_url'],
                main_category=company_dict['main_category'], status_fk=company_dict['status_fk'])
    await conn.execute(stmt)

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
