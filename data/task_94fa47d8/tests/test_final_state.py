# test_final_state.py

import os
import re
import pytest

HOME = '/home/user'
WEB_DIR = os.path.join(HOME, 'provisioned_web')
INDEX_HTML = os.path.join(WEB_DIR, 'index.html')
SERVER_LOG = os.path.join(WEB_DIR, 'server.log')
PROVISION_CHECK_LOG = os.path.join(WEB_DIR, 'provision_check.log')

INDEX_HTML_CONTENT = """<html>
<body>
<h1>Provisioned Service Ready</h1>
</body>
</html>
"""

@pytest.mark.final_state
def test_provisioned_web_directory_exists():
    assert os.path.isdir(WEB_DIR), (
        f"Directory {WEB_DIR} does not exist. "
        "You must create this directory as part of the provisioning."
    )

@pytest.mark.final_state
def test_index_html_exists_and_correct():
    assert os.path.isfile(INDEX_HTML), (
        f"{INDEX_HTML} does not exist. "
        "You must create this file with the specified content."
    )
    with open(INDEX_HTML, 'r', encoding='utf-8') as f:
        content = f.read()
    assert content == INDEX_HTML_CONTENT, (
        f"{INDEX_HTML} content is incorrect.\n"
        f"Expected:\n{INDEX_HTML_CONTENT!r}\n"
        f"Found:\n{content!r}"
    )

@pytest.mark.final_state
def test_server_log_exists_and_has_expected_entry():
    assert os.path.isfile(SERVER_LOG), (
        f"{SERVER_LOG} does not exist. "
        "The HTTP server must be started with output logged to this file."
    )
    with open(SERVER_LOG, 'r', encoding='utf-8') as f:
        log_content = f.read()
    # Look for line like: 'GET / HTTP/1.1" 200 -'
    # Accept HTTP/1.0 or HTTP/1.1, any client, and any timestamp
    get_line_re = re.compile(r'GET / HTTP/1\.[01]" 200 -')
    assert get_line_re.search(log_content), (
        f"{SERVER_LOG} does not show a GET / request being logged.\n"
        "After provisioning, there must be at least one line like:\n"
        '"GET / HTTP/1.1" 200 -\n'
        "Current log content:\n" + log_content
    )

@pytest.mark.final_state
def test_provision_check_log_exists_and_has_http_response():
    assert os.path.isfile(PROVISION_CHECK_LOG), (
        f"{PROVISION_CHECK_LOG} does not exist. "
        "You must store the HTTP response from GET http://localhost:8080/ including headers and body."
    )
    with open(PROVISION_CHECK_LOG, 'r', encoding='utf-8', errors='replace') as f:
        log_content = f.read()

    # Check for HTTP status line
    # Accept HTTP/1.0 or HTTP/1.1 200 OK
    status_line_re = re.compile(r'^HTTP/1\.[01] 200 OK', re.MULTILINE)
    assert status_line_re.search(log_content), (
        f"{PROVISION_CHECK_LOG} does not contain a valid HTTP status line.\n"
        "It must start with 'HTTP/1.0 200 OK' or 'HTTP/1.1 200 OK'.\n"
        f"Current content:\n{log_content}"
    )

    # Check for Server header (should mention SimpleHTTP and Python)
    server_header_re = re.compile(r'^Server:\s*SimpleHTTP/\d+\.\d+ Python/\d+\.\d+\.\d+', re.MULTILINE)
    assert server_header_re.search(log_content), (
        f"{PROVISION_CHECK_LOG} does not contain a valid Server header.\n"
        "It must include 'Server: SimpleHTTP/X.X Python/X.X.X'.\n"
        f"Current content:\n{log_content}"
    )

    # Check for Date header (should be present)
    date_header_re = re.compile(r'^Date:\s?.+', re.MULTILINE)
    assert date_header_re.search(log_content), (
        f"{PROVISION_CHECK_LOG} does not contain a Date header.\n"
        f"Current content:\n{log_content}"
    )

    # Check for Content-type header (should be text/html)
    content_type_re = re.compile(r'^Content-type:\s*text/html', re.MULTILINE)
    assert content_type_re.search(log_content), (
        f"{PROVISION_CHECK_LOG} does not contain a Content-type: text/html header.\n"
        f"Current content:\n{log_content}"
    )

    # Check that the body matches exactly the index.html content, and that it follows the headers after a blank line
    # HTTP headers end at the first blank line, then comes the body
    parts = re.split(r'\r?\n\r?\n', log_content, maxsplit=1)
    assert len(parts) == 2, (
        f"{PROVISION_CHECK_LOG} does not have a blank line separating headers and body.\n"
        f"Current content:\n{log_content}"
    )
    body = parts[1]
    # The body may end with a trailing newline, so strip it for comparison
    assert body.strip() == INDEX_HTML_CONTENT.strip(), (
        f"{PROVISION_CHECK_LOG} body does not match {INDEX_HTML}.\n"
        f"Expected body:\n{INDEX_HTML_CONTENT!r}\n"
        f"Found body:\n{body!r}"
    )