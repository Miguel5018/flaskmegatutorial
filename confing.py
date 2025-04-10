import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = int(os.environ.get("MAIL_PORT") or 25)
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") is not None
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    ADMINS = ["your-email@example.com"]
    LANGUAGES = ["en"]
    POSTS_PER_PAGE = 25
    MS_TRANSLATOR_KEY = "BQ9a3jeqozmTa1hzmhOpjpdDJ0LxYlbuyTICJn3col6zVKvIcF1sJQQJ99BCACYeBjFXJ3w3AAAbACOGdIwt"
    ELASTICSEARCH_URL = "http://elasticsearch:9200"
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
