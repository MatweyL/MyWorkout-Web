import os
import pathlib

from dotenv import load_dotenv


def get_project_root():
    return pathlib.Path(__file__).parent.parent.parent


def get_env_path():
    return os.path.join(get_project_root(), ".env")


def load_env():
    load_dotenv(get_env_path())


load_env()


def get_db_connection_params():
    return {"host": os.environ.get("DB_HOST"),
            "port": os.environ.get("DB_PORT"),
            "database": os.environ.get("DB_NAME"),
            "user": os.environ.get("DB_USER"),
            "passwd": os.environ.get("DB_PASSWORD")}


if __name__ == "__main__":
    print(get_db_connection_params())
