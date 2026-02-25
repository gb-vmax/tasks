# test_final_state.py

import os
import pwd
import pytest

DEPLOY_DIR = '/home/user/deploy'
ENV_FILE = '/home/user/deploy/.env.production'
LOG_FILE = '/home/user/deploy/env_check.log'

ENV_FILE_CONTENT = (
    "APP_ENV=production\n"
    "DB_HOST=db.prod.company.com\n"
    "DB_USER=release_manager\n"
    "DB_PASS=Sup3rS3cret!\n"
)

LOG_FILE_CONTENT = (
    "APP_ENV=production\n"
    "DB_HOST=db.prod.company.com\n"
    "DB_USER=release_manager\n"
    "DB_PASS=Sup3rS3cret!\n"
)

def get_owner(path):
    """Return username of the file/directory owner"""
    stat_info = os.stat(path)
    return pwd.getpwuid(stat_info.st_uid).pw_name

def read_file_exact(path):
    """Read the entire file, returning its content as a string (including newlines)."""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def test_deploy_directory_exists_and_owned():
    assert os.path.isdir(DEPLOY_DIR), (
        f"Directory {DEPLOY_DIR} does not exist or is not a directory."
    )
    owner = get_owner(DEPLOY_DIR)
    assert owner == 'user', (
        f"Directory {DEPLOY_DIR} exists but is owned by '{owner}', expected owner 'user'."
    )

def test_env_production_exists_and_content():
    assert os.path.isfile(ENV_FILE), (
        f"File {ENV_FILE} does not exist."
    )
    content = read_file_exact(ENV_FILE)
    assert content == ENV_FILE_CONTENT, (
        f"File {ENV_FILE} does not have the expected content.\n"
        f"Expected:\n{ENV_FILE_CONTENT!r}\n"
        f"Found:\n{content!r}\n"
        "Ensure each key-value pair is on its own line, with no extra spaces, quotes, or blank lines."
    )

def test_env_check_log_exists_and_content():
    assert os.path.isfile(LOG_FILE), (
        f"File {LOG_FILE} does not exist."
    )
    content = read_file_exact(LOG_FILE)
    assert content == LOG_FILE_CONTENT, (
        f"File {LOG_FILE} does not have the expected content.\n"
        f"Expected:\n{LOG_FILE_CONTENT!r}\n"
        f"Found:\n{content!r}\n"
        "The log file must contain only those four lines in the specified order, with no extra output or blank lines."
    )