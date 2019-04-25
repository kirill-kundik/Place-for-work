from sqlalchemy import create_engine, MetaData

from db.models import *
from backend.settings import BASE_DIR, get_config
from db.sample_data import get_sample_news, get_sample_categories

DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"

ADMIN_DB_URL = DSN.format(
    user='postgres', password='postgres', database='postgres',
    host='postgres', port=5432
)

admin_engine = create_engine(ADMIN_DB_URL, isolation_level='AUTOCOMMIT')

USER_CONFIG_PATH = BASE_DIR / 'config' / 'workplace.yaml'
USER_CONFIG = get_config(['-c', USER_CONFIG_PATH.as_posix()])
USER_DB_URL = DSN.format(**USER_CONFIG['postgres'])
user_engine = create_engine(USER_DB_URL)

TEST_CONFIG_PATH = BASE_DIR / 'config' / 'workplace_test.yaml'
TEST_CONFIG = get_config(['-c', TEST_CONFIG_PATH.as_posix()])
TEST_DB_URL = DSN.format(**TEST_CONFIG['postgres'])
test_engine = create_engine(TEST_DB_URL)


def setup_db(config):
    db_name = config['database']
    db_user = config['user']
    db_pass = config['password']

    conn = admin_engine.connect()
    conn.execute("DROP DATABASE IF EXISTS %s" % db_name)
    conn.execute("DROP ROLE IF EXISTS %s" % db_user)
    conn.execute("CREATE USER %s WITH PASSWORD '%s'" % (db_user, db_pass))
    conn.execute("CREATE DATABASE %s ENCODING 'UTF8'" % db_name)
    conn.execute("GRANT ALL PRIVILEGES ON DATABASE %s TO %s" %
                 (db_name, db_user))
    conn.close()


def teardown_db(config):
    db_name = config['database']
    db_user = config['user']

    conn = admin_engine.connect()
    conn.execute("""
      SELECT pg_terminate_backend(pg_stat_activity.pid)
      FROM pg_stat_activity
      WHERE pg_stat_activity.datname = '%s'
        AND pid <> pg_backend_pid();""" % db_name)
    conn.execute("DROP DATABASE IF EXISTS %s" % db_name)
    conn.execute("DROP ROLE IF EXISTS %s" % db_user)
    conn.close()


def create_tables(engine=test_engine):
    meta = MetaData()
    meta.create_all(bind=engine,
                    tables=[status, company, phones, address, category, working_type, vacancy, employer, resume,
                            resume_experience, response, messages, news, admin])


def drop_tables(engine=test_engine):
    meta = MetaData()
    meta.drop_all(bind=engine,
                  tables=[status, company, phones, address, category, working_type, vacancy, employer, resume,
                          resume_experience, response, messages, news, admin])


def sample_data(engine=test_engine):
    conn = engine.connect()
    conn.execute(admin.insert(), [
        {'email': 'admin@admin.com',
         'pass_hash': '$5$rounds=535000$hYkOykAwtwdNpZbd$N04R0fNDHWtpkGiGcIRVeg4ARkcwbhJCFDQYcgPnBOC'}
    ])
    conn.execute(status.insert(), [
        {'name': 'Активно шукаємо нових співробітників'},
        {'name': 'Шукаємо нових співробітників'},
        {'name': 'Поки що немає відкритих вакансій'}
    ])
    conn.execute(working_type.insert(), [
        {'name': 'Повна занятість'},
        {'name': 'Частково повна занятість (30 год / тиж)'},
        {'name': 'Неповна занятість'},
        {'name': 'Для студентів'}
    ])
    conn.execute(category.insert(), get_sample_categories())
    conn.execute(news.insert(), get_sample_news())
    conn.close()


def init_db():
    setup_db(USER_CONFIG['postgres'])
    create_tables(engine=user_engine)
    sample_data(engine=user_engine)
    # drop_tables()
    # teardown_db(config)


if __name__ == '__main__':
    init_db()
