from sqlalchemy import create_engine, MetaData

from db.models import *
from backend.settings import BASE_DIR, get_config

DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"

ADMIN_DB_URL = DSN.format(
    user='postgres', password='karpovich', database='postgres',
    host='localhost', port=5432
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
        {'name': 'Частково повна занятість (30 год на тиждень)'},
        {'name': 'Неповна занятість'},
        {'name': 'Для студентів'}
    ])
    conn.execute(category.insert(), [
        {
            'name': 'Python',
            'image_url': 'https://python.rs/pylogo.png',
            'description':
                """Python (найчастіше вживане прочитання — «Па́йтон», запозичено назву[5] з британського шоу Монті 
                Пайтон) — інтерпретована об\' єктно - орієнтована мова програмування високого рівня зі строгою 
                динамічною типізацією.[6] Розроблена в 1990 році Гвідо ван Россумом.Структури даних високого рівня 
                разом із динамічною семантикою та динамічним зв 'язуванням роблять її привабливою для швидкої 
                розробки програм, а також як засіб поєднування наявних компонентів. Python підтримує модулі та пакети 
                модулів, що сприяє модульності та повторному використанню коду. Інтерпретатор Python та стандартні 
                бібліотеки доступні як у скомпільованій, так і у вихідній формі на всіх основних платформах. В мові 
                програмування Python підтримується кілька парадигм програмування, зокрема: об\'єктно - орієнтована, 
                процедурна, функціональна та аспектно - орієнтована. """
        },
        {
            'name': 'Java',
            'image_url': 'https://cdn.lynda.com/course/184457/184457-636806635954727169-16x9.jpg',
            'description':
                """Java (вимовляється Джава[4]) — об'єктно-орієнтована мова програмування, випущена 1995 року 
                компанією «Sun Microsystems» як основний компонент платформи Java. З 2009 року мовою займається 
                компанія «Oracle», яка того року придбала «Sun Microsystems». В офіційній реалізації Java-програми 
                компілюються у байт-код, який при виконанні інтерпретується віртуальною машиною для конкретної 
                платформи. 
    
    «Oracle» надає компілятор Java та віртуальну машину Java, які задовольняють специфікації Java Community Process, 
    під ліцензією GNU General Public License. 
    
    Мова значно запозичила синтаксис із C і C++. Зокрема, взято за основу об'єктну модель С++, проте її модифіковано. 
    Усунуто можливість появи деяких конфліктних ситуацій, що могли виникнути через помилки програміста та полегшено 
    сам процес розробки об'єктно-орієнтованих програм. Ряд дій, які в С/C++ повинні здійснювати програмісти, 
    доручено віртуальній машині. Передусім Java розроблялась як платформо-незалежна мова, тому вона має менше 
    низькорівневих можливостей для роботи з апаратним забезпеченням, що в порівнянні, наприклад, з C++ зменшує 
    швидкість роботи програм. За необхідності таких дій Java дозволяє викликати підпрограми, написані іншими мовами 
    програмування. 
    
    Java вплинула на розвиток J++[en], що розроблялась компанією «Microsoft». Роботу над J++ було зупинено через 
    судовий позов «Sun Microsystems», оскільки ця мова програмування була модифікацією Java. Пізніше в новій 
    платформі «Microsoft» .NET випустили J#, щоб полегшити міграцію програмістів J++ або Java на нову платформу. З 
    часом нова мова програмування С# стала основною мовою платформи, перейнявши багато чого з Java. J# востаннє 
    включався в версію Microsoft Visual Studio 2005. Мова сценаріїв JavaScript має схожу із Java назву і синтаксис, 
    але не пов'язана із Java. """
        },
        {
            'name': 'C++',
            'image_url': 'https://media.geeksforgeeks.org/wp-content/cdn-uploads/titleShadow-1024x341.png',
            'description':
                """C++ (Сі-плюс-плюс) — мова програмування високого[1][2] рівня з підтримкою кількох парадигм 
                програмування: об'єктно-орієнтованої, узагальненої та процедурної. Розроблена Б'ярном Страуструпом (
                англ. Bjarne Stroustrup) в AT&T Bell Laboratories (Мюррей-Хілл, Нью-Джерсі) 1979 року та початково 
                отримала назву «Сі з класами». Згодом Страуструп перейменував мову на C++ у 1983 р. Базується на мові 
                С. Вперше описана стандартом ISO/IEC 14882:1998, найбільш актуальним же є стандарт ISO/IEC 
                14882:2014.[3] 
    
    У 1990-х роках С++ стала однією з найуживаніших мов програмування загального призначення. Мову використовують для 
    системного програмування, розробки програмного забезпечення, написання драйверів, потужних серверних та 
    клієнтських програм, а також для розробки розважальних програм, наприклад, відеоігор. С++ суттєво вплинула на 
    інші популярні сьогодні мови програмування: С# та Java. """
        }
    ])
    # TODO insert basic info while initialize db
    # conn.execute(question.insert(), [
    #     {'question_text': 'What\'s new?',
    #      'pub_date': '2015-12-15 17:17:49.629+02'}
    # ])
    # conn.execute(choice.insert(), [
    #     {'choice_text': 'Not much', 'votes': 0, 'question_id': 1},
    #     {'choice_text': 'The sky', 'votes': 0, 'question_id': 1},
    #     {'choice_text': 'Just hacking again', 'votes': 0, 'question_id': 1},
    # ])
    conn.close()


if __name__ == '__main__':
    setup_db(USER_CONFIG['postgres'])
    create_tables(engine=user_engine)
    sample_data(engine=user_engine)
    # drop_tables()
    # teardown_db(config)
