# test_final_state.py

import os
import pytest

BASE = "/home/user/dashboards"


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def readlink(rel_path):
    return os.readlink(os.path.join(BASE, rel_path))


def abspath(rel_path):
    return os.path.join(BASE, rel_path)


# ---------------------------------------------------------------------------
# Step 1 – Production symlinks
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("rel_path,expected_target", [
    ("active/production/nodes.json",    "../../templates/infra/nodes_v3.json"),
    ("active/production/latency.json",  "../../templates/app/latency_v2.json"),
    ("active/production/requests.json", "../../templates/app/requests_v3.json"),
    ("active/production/queries.json",  "../../templates/db/queries_v2.json"),
])
def test_production_symlinks(rel_path, expected_target):
    full = abspath(rel_path)
    assert os.path.islink(full), (
        f"Expected a symlink at {full} but it is not a symlink (or does not exist)."
    )
    actual = os.readlink(full)
    assert actual == expected_target, (
        f"Symlink {full} has wrong target.\n"
        f"  Expected: {expected_target!r}\n"
        f"  Got:      {actual!r}"
    )


# ---------------------------------------------------------------------------
# Step 2 – Staging symlinks
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("rel_path,expected_target", [
    ("active/staging/nodes.json",    "../../templates/infra/nodes_v2.json"),
    ("active/staging/latency.json",  "../../templates/app/latency_v2.json"),
    ("active/staging/requests.json", "../../templates/app/requests_v3.json"),
])
def test_staging_symlinks(rel_path, expected_target):
    full = abspath(rel_path)
    assert os.path.islink(full), (
        f"Expected a symlink at {full} but it is not a symlink (or does not exist)."
    )
    actual = os.readlink(full)
    assert actual == expected_target, (
        f"Symlink {full} has wrong target.\n"
        f"  Expected: {expected_target!r}\n"
        f"  Got:      {actual!r}"
    )


def test_staging_no_queries_symlink():
    """staging/queries.json should NOT exist."""
    full = abspath("active/staging/queries.json")
    assert not os.path.exists(full) and not os.path.islink(full), (
        f"{full} should not exist in staging, but it does."
    )


# ---------------------------------------------------------------------------
# Step 3 – Development symlinks
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("rel_path,expected_target", [
    ("active/development/latency.json",  "../../templates/app/latency_v2.json"),
    ("active/development/nodes.json",    "../../templates/infra/nodes_v2.json"),
    ("active/development/queries.json",  "../../templates/db/queries_v1.json"),
    ("active/development/requests.json", "../../templates/app/requests_v3.json"),
])
def test_development_symlinks(rel_path, expected_target):
    full = abspath(rel_path)
    assert os.path.islink(full), (
        f"Expected a symlink at {full} but it is not a symlink (or does not exist)."
    )
    actual = os.readlink(full)
    assert actual == expected_target, (
        f"Symlink {full} has wrong target.\n"
        f"  Expected: {expected_target!r}\n"
        f"  Got:      {actual!r}"
    )


def test_development_has_exactly_four_entries():
    dev_dir = abspath("active/development")
    entries = sorted(os.listdir(dev_dir))
    expected = sorted(["latency.json", "nodes.json", "queries.json", "requests.json"])
    assert entries == expected, (
        f"active/development/ should contain exactly {expected}, but found {entries}."
    )


# ---------------------------------------------------------------------------
# Step 4 – Archive nodes_v1.json
# ---------------------------------------------------------------------------

def test_archive_nodes_v1_is_regular_file():
    full = abspath("archive/nodes_v1.json")
    assert os.path.isfile(full) and not os.path.islink(full), (
        f"Expected a regular (non-symlink) file at {full}."
    )


def test_archive_nodes_v1_content():
    full = abspath("archive/nodes_v1.json")
    with open(full) as f:
        content = f.read().strip()
    expected = '{"dashboard":"nodes","version":1}'
    assert content == expected, (
        f"archive/nodes_v1.json has unexpected content.\n"
        f"  Expected: {expected!r}\n"
        f"  Got:      {content!r}"
    )


def test_templates_infra_nodes_v1_is_symlink():
    full = abspath("templates/infra/nodes_v1.json")
    assert os.path.islink(full), (
        f"Expected {full} to be a symlink (pointing to the archive), "
        f"but it is not a symlink."
    )


def test_templates_infra_nodes_v1_symlink_target():
    full = abspath("templates/infra/nodes_v1.json")
    actual = os.readlink(full)
    expected = "../../archive/nodes_v1.json"
    assert actual == expected, (
        f"Symlink {full} has wrong target.\n"
        f"  Expected: {expected!r}\n"
        f"  Got:      {actual!r}"
    )


def test_templates_infra_nodes_v1_resolves_to_archive():
    """The symlink must actually resolve to the archived file."""
    full = abspath("templates/infra/nodes_v1.json")
    resolved = os.path.realpath(full)
    archive_file = os.path.realpath(abspath("archive/nodes_v1.json"))
    assert resolved == archive_file, (
        f"templates/infra/nodes_v1.json does not resolve to archive/nodes_v1.json.\n"
        f"  Resolved to: {resolved}\n"
        f"  Expected:    {archive_file}"
    )


# ---------------------------------------------------------------------------
# Step 5 – Audit report
# ---------------------------------------------------------------------------

EXPECTED_REPORT = """\
=== Dashboard Symlink Audit ===

[development]
  latency.json -> ../../templates/app/latency_v2.json
  nodes.json -> ../../templates/infra/nodes_v2.json
  queries.json -> ../../templates/db/queries_v1.json
  requests.json -> ../../templates/app/requests_v3.json

[production]
  latency.json -> ../../templates/app/latency_v2.json
  nodes.json -> ../../templates/infra/nodes_v3.json
  queries.json -> ../../templates/db/queries_v2.json
  requests.json -> ../../templates/app/requests_v3.json

[staging]
  latency.json -> ../../templates/app/latency_v2.json
  nodes.json -> ../../templates/infra/nodes_v2.json
  requests.json -> ../../templates/app/requests_v3.json

Total symlinks: 11
"""


def test_audit_report_exists():
    full = abspath("audit_report.txt")
    assert os.path.isfile(full), (
        f"audit_report.txt does not exist at {full}."
    )


def test_audit_report_exact_content():
    full = abspath("audit_report.txt")
    with open(full) as f:
        content = f.read()
    assert content == EXPECTED_REPORT, (
        f"audit_report.txt content does not match expected.\n"
        f"--- EXPECTED ---\n{EXPECTED_REPORT!r}\n"
        f"--- GOT ---\n{content!r}"
    )


def test_audit_report_line_count():
    full = abspath("audit_report.txt")
    with open(full) as f:
        lines = f.readlines()
    # 20 lines including the trailing newline (last line ends with \n)
    assert len(lines) == 20, (
        f"audit_report.txt should have exactly 20 lines, but has {len(lines)}.\n"
        f"Lines: {lines}"
    )


def test_audit_report_total_symlinks_line():
    full = abspath("audit_report.txt")
    with open(full) as f:
        content = f.read()
    assert "Total symlinks: 11" in content, (
        f"audit_report.txt does not contain 'Total symlinks: 11'.\n"
        f"Content:\n{content}"
    )


# ---------------------------------------------------------------------------
# Sanity – other template files still exist as regular files
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("rel_path,expected_content", [
    ("templates/infra/nodes_v2.json", '{"dashboard":"nodes","version":2}'),
    ("templates/infra/nodes_v3.json", '{"dashboard":"nodes","version":3}'),
    ("templates/app/latency_v1.json", '{"dashboard":"latency","version":1}'),
    ("templates/app/latency_v2.json", '{"dashboard":"latency","version":2}'),
    ("templates/app/requests_v1.json", '{"dashboard":"requests","version":1}'),
    ("templates/app/requests_v2.json", '{"dashboard":"requests","version":2}'),
    ("templates/app/requests_v3.json", '{"dashboard":"requests","version":3}'),
    ("templates/db/queries_v1.json", '{"dashboard":"queries","version":1}'),
    ("templates/db/queries_v2.json", '{"dashboard":"queries","version":2}'),
])
def test_template_files_intact(rel_path, expected_content):
    full = abspath(rel_path)
    assert os.path.isfile(full), f"Expected regular file missing: {full}"
    with open(full) as f:
        content = f.read().strip()
    assert content == expected_content, (
        f"File {full} has unexpected content.\n"
        f"  Expected: {expected_content!r}\n"
        f"  Got:      {content!r}"
    )


# ---------------------------------------------------------------------------
# Sanity – directory structure still intact
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("rel_dir", [
    "templates/infra",
    "templates/app",
    "templates/db",
    "active/production",
    "active/staging",
    "active/development",
    "archive",
])
def test_directory_exists(rel_dir):
    full = abspath(rel_dir)
    assert os.path.isdir(full), f"Expected directory missing: {full}"