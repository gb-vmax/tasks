# test_final_state.py

import os
import pwd
import stat
import pytest

HOME = '/home/user'
SOURCE_CONFIGS = os.path.join(HOME, 'source_configs')
NGINX_CONF = os.path.join(SOURCE_CONFIGS, 'nginx.conf')
REMOTE_CONFIGS = os.path.join(HOME, 'remote_server', 'configs')
REMOTE_NGINX_CONF = os.path.join(REMOTE_CONFIGS, 'nginx.conf')
SYNC_LOG = os.path.join(HOME, 'sync.log')

NGINX_CONF_CONTENT = (
    "user www-data;\n"
    "worker_processes auto;\n"
    "pid /run/nginx.pid;\n"
)

SYNC_LOG_CONTENT = f"COPIED: {REMOTE_NGINX_CONF}\n"

def get_owner(path):
    stat_info = os.stat(path)
    return pwd.getpwuid(stat_info.st_uid).pw_name

def get_dir_listing(path):
    # Only return non-hidden files/directories
    return sorted([f for f in os.listdir(path) if not f.startswith('.')])

def check_permissions(path, expected=0o755):
    st_mode = os.stat(path).st_mode
    # Accept 755 or 775 (default umask may be 002)
    return stat.S_IMODE(st_mode) == expected or stat.S_IMODE(st_mode) == 0o775

@pytest.mark.finalstate
def test_source_configs_dir_exists_and_owned():
    assert os.path.isdir(SOURCE_CONFIGS), (
        f"Directory {SOURCE_CONFIGS} does not exist."
    )
    owner = get_owner(SOURCE_CONFIGS)
    assert owner == 'user', (
        f"Directory {SOURCE_CONFIGS} is not owned by user (found owner: {owner})."
    )
    assert check_permissions(SOURCE_CONFIGS), (
        f"Permissions for {SOURCE_CONFIGS} are not 755 or 775 (found: {oct(stat.S_IMODE(os.stat(SOURCE_CONFIGS).st_mode))})."
    )

@pytest.mark.finalstate
def test_source_configs_contains_only_nginx_conf():
    contents = get_dir_listing(SOURCE_CONFIGS)
    assert contents == ['nginx.conf'], (
        f"{SOURCE_CONFIGS} should contain only 'nginx.conf', found: {contents}."
    )

@pytest.mark.finalstate
def test_nginx_conf_exists_and_content():
    assert os.path.isfile(NGINX_CONF), (
        f"File {NGINX_CONF} does not exist."
    )
    owner = get_owner(NGINX_CONF)
    assert owner == 'user', (
        f"File {NGINX_CONF} is not owned by user (found owner: {owner})."
    )
    with open(NGINX_CONF, 'r', encoding='utf-8') as f:
        content = f.read()
    assert content == NGINX_CONF_CONTENT, (
        f"Contents of {NGINX_CONF} do not match expected.\n"
        f"Expected:\n{repr(NGINX_CONF_CONTENT)}\nFound:\n{repr(content)}"
    )

@pytest.mark.finalstate
def test_remote_configs_dir_exists_and_owned():
    assert os.path.isdir(REMOTE_CONFIGS), (
        f"Directory {REMOTE_CONFIGS} does not exist."
    )
    owner = get_owner(REMOTE_CONFIGS)
    assert owner == 'user', (
        f"Directory {REMOTE_CONFIGS} is not owned by user (found owner: {owner})."
    )
    assert check_permissions(REMOTE_CONFIGS), (
        f"Permissions for {REMOTE_CONFIGS} are not 755 or 775 (found: {oct(stat.S_IMODE(os.stat(REMOTE_CONFIGS).st_mode))})."
    )

@pytest.mark.finalstate
def test_remote_configs_contains_only_nginx_conf():
    contents = get_dir_listing(REMOTE_CONFIGS)
    assert contents == ['nginx.conf'], (
        f"{REMOTE_CONFIGS} should contain only 'nginx.conf', found: {contents}."
    )

@pytest.mark.finalstate
def test_remote_nginx_conf_exists_and_content():
    assert os.path.isfile(REMOTE_NGINX_CONF), (
        f"File {REMOTE_NGINX_CONF} does not exist."
    )
    owner = get_owner(REMOTE_NGINX_CONF)
    assert owner == 'user', (
        f"File {REMOTE_NGINX_CONF} is not owned by user (found owner: {owner})."
    )
    with open(REMOTE_NGINX_CONF, 'r', encoding='utf-8') as f:
        content = f.read()
    assert content == NGINX_CONF_CONTENT, (
        f"Contents of {REMOTE_NGINX_CONF} do not match expected.\n"
        f"Expected:\n{repr(NGINX_CONF_CONTENT)}\nFound:\n{repr(content)}"
    )

@pytest.mark.finalstate
def test_no_extra_files_in_source_configs():
    contents = get_dir_listing(SOURCE_CONFIGS)
    assert contents == ['nginx.conf'], (
        f"Extra files or directories found in {SOURCE_CONFIGS}: {contents} (should contain only 'nginx.conf')."
    )

@pytest.mark.finalstate
def test_no_extra_files_in_remote_configs():
    contents = get_dir_listing(REMOTE_CONFIGS)
    assert contents == ['nginx.conf'], (
        f"Extra files or directories found in {REMOTE_CONFIGS}: {contents} (should contain only 'nginx.conf')."
    )

@pytest.mark.finalstate
def test_sync_log_exists_and_content():
    assert os.path.isfile(SYNC_LOG), (
        f"File {SYNC_LOG} does not exist."
    )
    owner = get_owner(SYNC_LOG)
    assert owner == 'user', (
        f"File {SYNC_LOG} is not owned by user (found owner: {owner})."
    )
    with open(SYNC_LOG, 'r', encoding='utf-8') as f:
        content = f.read()
    assert content == SYNC_LOG_CONTENT, (
        f"Contents of {SYNC_LOG} do not match expected.\n"
        f"Expected:\n{repr(SYNC_LOG_CONTENT)}\nFound:\n{repr(content)}"
    )

@pytest.mark.finalstate
def test_sync_log_no_extra_lines():
    with open(SYNC_LOG, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    assert len(lines) == 1, (
        f"{SYNC_LOG} should contain only 1 line, found {len(lines)} line(s): {lines}"
    )
    assert lines[0] == SYNC_LOG_CONTENT, (
        f"Line in {SYNC_LOG} does not match expected.\n"
        f"Expected: {repr(SYNC_LOG_CONTENT)}\nFound: {repr(lines[0])}"
    )