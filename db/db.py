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
    INSERT INTO vacancy(position, description, requirements, salary, working_type_fk, company_fk, category_fk, date) 
    VALUES ('%s', '%s', '%s', '%s', %s, (SELECT id FROM company WHERE email = '%s'), %s, NOW()) 
    RETURNING id, category_fk, (SELECT name FROM category WHERE id = category_fk), 
    (SELECT name FROM working_type WHERE id = working_type_fk), (SELECT name FROM company WHERE id = company_fk),
     company_fk
    """ % (vacancy_dict['position'], vacancy_dict['description'], vacancy_dict['requirements'], vacancy_dict['salary'],
           vacancy_dict['working_type_fk'], email, vacancy_dict['category_fk'])
    res = await conn.execute(stmt)
    return await res.fetchone()


async def create_resume(conn, resume_dict, email):
    stmt = """
    INSERT INTO resume(perks, hobbies, category_fk, employer_fk) 
    VALUES ('%s', '%s', %s, (SELECT id FROM employer WHERE email = '%s'))
    RETURNING id
    """ % (resume_dict['perks'], resume_dict['hobbies'], resume_dict['category_fk'], email)
    res = await conn.execute(stmt)
    return await res.fetchone()


async def create_resume_experience(conn, exp_dict):
    stmt = models.resume_experience.insert().values(**exp_dict)
    await conn.execute(stmt)


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


async def get_company_by_id(conn, c_id):
    check = await conn.execute(
        models.company.select().where(models.company.c.id == c_id)
    )
    res = await check.fetchone()
    if not res:
        raise UserDoesNotExistsException
    return res


async def get_companies(conn):
    res = await conn.execute(models.company.select())
    return await res.fetchall()


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
    wt.name AS working_type, c.name AS category_name, c.id AS category_id 
    FROM vacancy v 
    INNER JOIN category c on v.category_fk = c.id 
    INNER JOIN company c2 on v.company_fk = c2.id
    INNER JOIN working_type wt on v.working_type_fk = wt.id
    WHERE v.id = %s
    """ % v_id
    res = await conn.execute(stmt)
    return await res.fetchone()


async def get_vacancies_by_cat_id(conn, cat_id, limit=0):
    stmt = """
    SELECT v.id, v.position, v.description, v.requirements, v.salary, c2.name AS company_name, c2.id AS company_id,
    wt.name AS work_type, c.name AS category_name, c.id AS category_id 
    FROM vacancy v 
    INNER JOIN category c on v.category_fk = c.id 
    INNER JOIN company c2 on v.company_fk = c2.id
    INNER JOIN working_type wt on v.working_type_fk = wt.id
    WHERE c.id = %s
    """ % cat_id
    if limit != 0:
        stmt = stmt + f" LIMIT {limit}"
    res = await conn.execute(stmt)
    return await res.fetchall()


async def get_vacancies_by_comp_id(conn, comp_id, limit=0):
    stmt = """
    SELECT v.id, v.position, v.description, v.requirements, v.salary, c2.name AS company_name, c2.id AS company_id,
    wt.name AS work_type, c.name AS category_name, c.id AS category_id 
    FROM vacancy v 
    INNER JOIN category c on v.category_fk = c.id 
    INNER JOIN company c2 on v.company_fk = c2.id
    INNER JOIN working_type wt on v.working_type_fk = wt.id
    WHERE c2.id = %s
    """ % comp_id
    if limit != 0:
        stmt = stmt + f" LIMIT {limit}"
    res = await conn.execute(stmt)
    return await res.fetchall()


async def get_vacancies(conn, limit=0):
    stmt = """
    SELECT v.id, v.position, v.description, v.requirements, v.salary, c2.name AS company_name, c2.id AS company_id,
    wt.name AS work_type, c.name AS category_name, c.id AS category_id 
    FROM vacancy v 
    INNER JOIN category c on v.category_fk = c.id 
    INNER JOIN company c2 on v.company_fk = c2.id
    INNER JOIN working_type wt on v.working_type_fk = wt.id
    """
    if limit != 0:
        stmt = stmt + f' LIMIT {limit}'
    res = await conn.execute(stmt)
    return await res.fetchall()


async def get_employer_resumes(conn, e_id):
    stmt = """
    SELECT id, perks, hobbies, category_fk AS category_id, 
    (SELECT name FROM category WHERE category.id = category_fk) AS category_name 
    FROM resume
    WHERE employer_fk = %s
    """ % e_id
    res = await conn.execute(stmt)
    return await res.fetchall()


async def get_resume(conn, r_id):
    stmt = """
    SELECT id, perks, hobbies, category_fk AS category_id, 
    (SELECT name FROM category WHERE category.id = category_fk) AS category_name FROM resume WHERE id = %s
    """ % (r_id,)
    res = await conn.execute(stmt)
    return await res.fetchone()


async def get_resume_experience(conn, r_id):
    stmt = models.resume_experience.select().where(models.resume_experience.c.resume_fk == r_id)
    res = await conn.execute(stmt)
    return await res.fetchall()


async def get_response(conn, email, vacancy_fk):
    stmt = """
    SELECT * FROM response resp
    WHERE vacancy_fk = %s
    AND resume_fk = (SELECT id FROM resume r WHERE r.category_fk = 
    (SELECT category_fk FROM vacancy WHERE id = resp.vacancy_fk) 
    AND r.employer_fk = (SELECT id FROM employer WHERE email = '%s'))
    """ % (vacancy_fk, email)
    res = await conn.execute(stmt)
    return serialize_row(await res.fetchone())


async def get_employer_responses(conn, email):
    stmt = """
    SELECT * FROM response
    WHERE resume_fk IN (SELECT id FROM resume WHERE employer_fk = (SELECT id FROM employer WHERE email = '%s'))
    """ % email
    res = await conn.execute(stmt)
    return await res.fetchall()


async def get_vacancy_responses(conn, v_id):
    result = await conn.execute(models.response.select().where(models.response.c.vacancy_fk == v_id))
    return await result.fetchall()


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


async def update_response(conn, r_id, response):
    await conn.execute(models.response.update()
                       .where(models.response.c.id == r_id)
                       .values(status=response['status'], entry_msg=response['entry_msg'],
                               interview_date=response['interview_date']))


async def check_employer_resume(conn, email, uid):
    stmt = """
    SELECT id FROM resume WHERE employer_fk = (SELECT id FROM employer WHERE employer.email = '%s') AND id = %s
    """ % (email, uid)
    res = await conn.execute(stmt)
    ids = await res.fetchone()
    if not ids:
        return False
    return True


async def check_employer_response(conn, email, vac_id):
    stmt = """
    SELECT id
    FROM response
    WHERE vacancy_fk = %s AND resume_fk IN 
        (SELECT id 
        FROM resume 
        WHERE employer_fk = 
            (SELECT id 
            FROM employer 
            WHERE email = '%s'))
    """ % (vac_id, email)
    res = await conn.execute(stmt)
    result = await res.fetchone()
    if result:
        return True
    return False


async def check_company_response(conn, email, r_id):
    stmt = """
    SELECT * 
    FROM response
    WHERE id = %s
    AND vacancy_fk IN (SELECT id FROM vacancy WHERE company_fk = (SELECT id FROM company WHERE email = '%s'))
    """ % (r_id, email)
    res = await conn.execute(stmt)
    result = await res.fetchone()
    if result:
        return True
    return False


async def check_company_resume(conn, email, r_id):
    stmt = """
    SELECT id 
    FROM resume 
    WHERE id IN (SELECT resume_fk 
                 FROM response 
                 WHERE vacancy_fk IN 
                            (SELECT id 
                            FROM vacancy 
                            WHERE company_fk = 
                                        (SELECT id 
                                        FROM company 
                                        WHERE email = '%s')))
    AND id = %s
    """ % (email, r_id)
    res = await conn.execute(stmt)
    result = await res.fetchone()
    if result:
        return True
    return False


async def check_employer_category_resume(conn, email, c_id):
    stmt = """
    SELECT id 
    FROM resume
    WHERE category_fk = %s
    AND employer_fk = (SELECT id FROM employer WHERE email = '%s')
    """ % (c_id, email)
    res = await conn.execute(stmt)
    result = await res.fetchone()
    if result:
        return True
    return False


async def check_employer_response_by_id(conn, email, res_id):
    stmt = """
    SELECT id FROM response
    WHERE id = %s
    AND resume_fk IN (SELECT id FROM resume WHERE employer_fk = (SELECT id FROM employer WHERE email = '%s')) 
    """ % (res_id, email)
    res = await conn.execute(stmt)
    result = await res.fetchone()
    if result:
        return True
    return False


async def check_company_vacancy(conn, email, v_id):
    stmt = """
    SELECT id FROM vacancy
    WHERE id = %s
    AND company_fk = (SELECT id FROM company WHERE email = '%s')
    """ % (v_id, email)
    res = await conn.execute(stmt)
    result = await res.fetchone()
    if result:
        return True
    return False


async def delete_response(conn, email, res_id):
    made_response = await check_employer_response_by_id(conn, email, res_id)
    if made_response:
        stmt = """
        DELETE FROM response WHERE id = %s
        """ % res_id
        await conn.execute(stmt)


async def make_response(conn, email, vac_id):
    made_response = await check_employer_response(conn, email, vac_id)
    if not made_response:
        vacancy = await get_vacancy(conn, vac_id)
        if await check_employer_category_resume(conn, email, vacancy['category_id']):
            stmt = """
            INSERT INTO response(resume_fk, vacancy_fk) 
            VALUES ((SELECT id 
                     FROM resume 
                     WHERE category_fk = %s AND employer_fk = (SELECT id 
                                                               FROM employer 
                                                               WHERE email = '%s')), %s)
            """ % (vacancy['category_id'], email, vac_id)
            await conn.execute(stmt)


def serialize_row(row):
    return {column: value for column, value in row.items()}
