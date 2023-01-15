from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#from utils import logger as log


try:

    SQL_ALCHAMY_DATABASE_URL = f'mssql://user_one:123456@SMPROVOC/test_db?driver=ODBC Driver 17 for SQL Server'

    engine = create_engine(SQL_ALCHAMY_DATABASE_URL, echo=False)

    Session = sessionmaker(bind=engine)
    session = Session()


    Base = declarative_base()
    Base.metadata.create_all(engine)

except Exception as e:
    log.events_logger.warning(f'[database connection] {e.args[0]}')

