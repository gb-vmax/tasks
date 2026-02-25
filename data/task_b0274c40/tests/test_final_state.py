# test_final_state.py

import os
import stat
import re
import pytest
from datetime import datetime

I18N_DIR = "/home/user/projects/i18n"
PO_FILE = "/home/user/projects/i18n/en_US.po"
LOG_FILE = "/home/user/projects/i18n/update_log.txt"

@pytest.mark.describe("Final filesystem and content state after student action")
class TestFinalState:
    def test_i18n_directory_exists(self):
        assert os.path.isdir(I18N_DIR), (
            f"Directory {I18N_DIR} does not exist. "
            "The i18n directory must be present at /home/user/projects/i18n."
        )

    def test_en_us_po_exists_and_permissions(self):
        assert os.path.isfile(PO_FILE), (
            f"File {PO_FILE} does not exist. "
            "The translation file en_US.po must exist at /home/user/projects/i18n/en_US.po."
        )
        st = os.stat(PO_FILE)
        expected_mode = 0o100644  # regular file with 644 permissions
        actual_mode = stat.S_IFMT(st.st_mode) | (st.st_mode & 0o777)
        assert actual_mode == expected_mode, (
            f"File {PO_FILE} should have permissions 644 (-rw-r--r--), "
            f"but has {oct(st.st_mode & 0o777)}."
        )

    def test_en_us_po_greeting_entry_sanitized(self):
        """Ensure msgid 'greeting' has no <script> tags in msgstr and is properly sanitized."""
        greeting_msgid = 'msgid "greeting"'
        sanitized_msgstr = 'msgstr "Welcome to our site! "'
        found_greeting = False
        found_script_tag = False
        with open(PO_FILE, encoding="utf-8") as f:
            lines = [line.rstrip('\n') for line in f]
        for i, line in enumerate(lines):
            if line == greeting_msgid:
                found_greeting = True
                # Search next few lines for the msgstr
                for j in range(i+1, min(i+5, len(lines))):
                    msgstr_line = lines[j].strip()
                    if msgstr_line.startswith('msgstr'):
                        # Check for <script> tag in msgstr
                        if re.search(r'<\s*script', msgstr_line, re.IGNORECASE):
                            found_script_tag = True
                        assert msgstr_line == sanitized_msgstr, (
                            f"The msgstr for msgid 'greeting' must be sanitized to:\n"
                            f'{sanitized_msgstr}\n'
                            f"But found:\n{msgstr_line}"
                        )
                        break
                break
        assert found_greeting, (
            f"Could not find msgid 'greeting' in {PO_FILE}. "
            "The entry must exist after sanitization."
        )
        assert not found_script_tag, (
            f"The msgstr for msgid 'greeting' in {PO_FILE} still contains a <script> tag. "
            "Sanitize all <script> tags from msgstr values."
        )

    def test_en_us_po_no_script_tags_anywhere(self):
        """Ensure there are no <script> tags in any msgstr in the .po file."""
        with open(PO_FILE, encoding="utf-8") as f:
            for lineno, line in enumerate(f, 1):
                if line.strip().startswith('msgstr'):
                    if re.search(r'<\s*script', line, re.IGNORECASE):
                        pytest.fail(
                            f"Found a <script> tag in msgstr on line {lineno} of {PO_FILE}: {line.strip()}\n"
                            "All <script> tags must be removed from msgstr values."
                        )

    def test_update_log_txt_exists_and_permissions(self):
        assert os.path.isfile(LOG_FILE), (
            f"Log file {LOG_FILE} does not exist. "
            "You must create the log file at /home/user/projects/i18n/update_log.txt after sanitizing."
        )
        st = os.stat(LOG_FILE)
        # Permissions: world-readable (at least 644)
        mode = stat.S_IMODE(st.st_mode)
        assert mode & 0o444 == 0o444, (
            f"Log file {LOG_FILE} must be world-readable (permissions at least 644), "
            f"but has {oct(mode)}."
        )

    def test_update_log_txt_content_exact(self):
        """Validate the log file content matches the required format and content."""
        required_msgid = "greeting"
        original_msgstr = "Welcome to our site! <script>alert('XSS');</script>"
        sanitized_msgstr = "Welcome to our site! "

        # Read log file content
        with open(LOG_FILE, encoding="utf-8") as f:
            log_content = f.read().rstrip('\n')

        # Split into lines and check count
        log_lines = log_content.split('\n')
        assert len(log_lines) == 4, (
            f"Log file {LOG_FILE} must have exactly 4 lines, but found {len(log_lines)}.\n"
            f"Content:\n{log_content}"
        )

        # DATE line: DATE: <YYYY-MM-DD HH:MM:SS>
        date_line = log_lines[0]
        assert date_line.startswith("DATE: "), (
            "First line of log must start with 'DATE: '"
        )
        date_str = date_line[6:]
        # Check date/time format
        try:
            dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
            # Optionally, ensure date is not in the future
            now = datetime.now()
            assert dt <= now, (
                f"The DATE in the log ({date_str}) is in the future. "
                "It should be the local system time at the time of update."
            )
        except ValueError:
            pytest.fail(
                f"DATE line in {LOG_FILE} does not match required format 'YYYY-MM-DD HH:MM:SS':\n"
                f"{date_line}"
            )

        # MSGID line: MSGID: greeting
        msgid_line = log_lines[1]
        assert msgid_line == f"MSGID: {required_msgid}", (
            f"Second line of log must be 'MSGID: {required_msgid}', but got: {msgid_line}"
        )

        # ORIGINAL line: ORIGINAL: Welcome to our site! <script>alert('XSS');</script>
        original_line = log_lines[2]
        assert original_line == f"ORIGINAL: {original_msgstr}", (
            f"Third line of log must be 'ORIGINAL: {original_msgstr}', but got: {original_line}"
        )

        # SANITIZED line: SANITIZED: Welcome to our site!
        sanitized_line = log_lines[3]
        assert sanitized_line == f"SANITIZED: {sanitized_msgstr}", (
            f"Fourth line of log must be 'SANITIZED: {sanitized_msgstr}', but got: {sanitized_line}"
        )