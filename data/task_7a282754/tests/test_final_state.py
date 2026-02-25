# test_final_state.py

import os
import stat
import pwd
import pytest
import sqlite3
import subprocess

DB_PATH = '/home/user/projects/tasks.db'
EXPECTED_OWNER = 'user'
EXPECTED_MODE = 0o644

EXPECTED_ROWS = [
    (1, 'main.py', 'alpha', '2024-05-01'),
    (2, 'README.md', 'alpha', '2024-05-02'),
    (3, 'utils.py', 'beta', '2024-05-03'),
]

EXPECTED_HEADER = 'id,filename,project,date_added'
EXPECTED_OUTPUT_LINES = [
    'id,filename,project,date_added',
    '1,main.py,alpha,2024-05-01',
    '2,README.md,alpha,2024-05-02',
    '3,utils.py,beta,2024-05-03',
]


def test_db_file_exists_and_permissions():
    """Check database file exists, is owned by user, and has mode 0644."""
    assert os.path.isfile(DB_PATH), (
        f"Missing required SQLite database file at {DB_PATH}."
    )
    st = os.stat(DB_PATH)
    uid = st.st_uid
    mode = stat.S_IMODE(st.st_mode)
    try:
        owner = pwd.getpwuid(uid).pw_name
    except KeyError:
        pytest.fail(f"Owner UID {uid} of {DB_PATH} does not correspond to a valid user.")

    assert owner == EXPECTED_OWNER, (
        f"{DB_PATH} must be owned by user '{EXPECTED_OWNER}', but is owned by '{owner}'."
    )
    assert mode == EXPECTED_MODE, (
        f"{DB_PATH} must have mode 0644, but has mode {oct(mode)}."
    )


def test_files_table_schema_and_content():
    """Check the schema and contents of the 'files' table are as required."""
    assert os.path.isfile(DB_PATH), (
        f"Cannot check database; {DB_PATH} does not exist."
    )
    conn = sqlite3.connect(DB_PATH)
    try:
        # Check schema
        cur = conn.execute("PRAGMA table_info(files);")
        columns = [(row[1], row[2], row[3], row[5]) for row in cur.fetchall()]
        expected_columns = [
            ('id', 'INTEGER', 0, 1),
            ('filename', 'TEXT', 1, 0),
            ('project', 'TEXT', 1, 0),
            ('date_added', 'TEXT', 1, 0)
        ]
        assert columns == expected_columns, (
            f"The 'files' table must have columns and constraints as:\n"
            f"  id INTEGER PRIMARY KEY,\n"
            f"  filename TEXT NOT NULL,\n"
            f"  project TEXT NOT NULL,\n"
            f"  date_added TEXT NOT NULL\n"
            f"Actual columns: {columns}"
        )

        # Check content
        cur = conn.execute("SELECT id, filename, project, date_added FROM files ORDER BY id;")
        rows = cur.fetchall()
        assert rows == EXPECTED_ROWS, (
            f"The 'files' table must contain the rows:\n"
            f"{EXPECTED_ROWS}\n"
            f"Actual rows:\n{rows}"
        )
    finally:
        conn.close()


def test_csv_report_output(monkeypatch):
    """Check that the student's script prints the correct CSV to stdout, with no extra output."""
    # Try to guess the student's script location
    possible_scripts = [
        '/home/user/report_files.py',
        '/home/user/projects/report_files.py',
        '/home/user/projects/files_report.py',
        '/home/user/projects/generate_csv.py',
        '/home/user/files_report.py',
        '/home/user/report.py',
    ]
    script_path = None
    for candidate in possible_scripts:
        if os.path.isfile(candidate):
            script_path = candidate
            break

    if script_path is None:
        pytest.skip(
            "Could not find the student's report script in any expected location. "
            "Please ensure the script exists and has the correct name."
        )

    # Run the script and capture output
    proc = subprocess.run(
        ['python3', script_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding='utf-8'
    )

    # Check for unexpected stderr
    if proc.stderr.strip():
        pytest.fail(
            f"Your script must not print anything to stderr. Got:\n{proc.stderr}"
        )

    # Split stdout into lines, stripping trailing newlines
    output_lines = proc.stdout.rstrip('\n').split('\n')

    # Check number of lines
    assert output_lines == EXPECTED_OUTPUT_LINES, (
        f"CSV output is not correct.\n"
        f"Expected:\n" +
        "\n".join(EXPECTED_OUTPUT_LINES) +
        "\nGot:\n" +
        "\n".join(output_lines)
    )

    # Check for blank lines at start or end
    if proc.stdout.startswith('\n') or proc.stdout.endswith('\n\n'):
        pytest.fail(
            "Your script's output has unexpected blank lines at start or end."
        )

    # Check for trailing spaces
    for i, line in enumerate(output_lines):
        if line != line.rstrip(' '):
            pytest.fail(
                f"Line {i+1} of your output has trailing spaces: {repr(line)}"
            )

    # Check for extra columns (headers and data)
    header_fields = output_lines[0].split(',')
    assert header_fields == ['id', 'filename', 'project', 'date_added'], (
        f"Header row must be: {EXPECTED_HEADER}\nGot: {output_lines[0]}"
    )

    for i, row in enumerate(output_lines[1:], 2):  # skip header
        fields = row.split(',')
        assert len(fields) == 4, (
            f"Row {i} must have exactly 4 columns. Got {len(fields)} columns: {fields}"
        )