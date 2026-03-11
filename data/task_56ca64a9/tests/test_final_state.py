# test_final_state.py

import os
import pytest

BACKUP_CONFIG_PATH = "/home/user/backups/backup_config.yaml"
RETENTION_TOML_PATH = "/home/user/backups/retention.toml"

EXPECTED_BACKUP_CONFIG = """\
database:
  host: postgres-primary.internal
  port: 5432
  name: appdb
retention_days: 30
schedule: "0 2 * * *"
storage:
  bucket: db-backups-prod-v2
  region: us-east-2
  encryption: true
notifications:
  email: dba-team@company.com
  on_failure: true"""

EXPECTED_RETENTION_TOML = """\
enabled = true
version = "2.0"

[policy.daily]
keep_days = 14
compress = true

[policy.weekly]
keep_days = 60
compress = true

[policy.monthly]
keep_days = 365
compress = false"""


# ── Directory / file existence ────────────────────────────────────────────────

def test_backups_directory_exists():
    backup_dir = "/home/user/backups"
    assert os.path.isdir(backup_dir), (
        f"Directory '{backup_dir}' does not exist. "
        "The backups directory must be present after the task."
    )


def test_backup_config_yaml_exists():
    assert os.path.isfile(BACKUP_CONFIG_PATH), (
        f"File '{BACKUP_CONFIG_PATH}' does not exist. "
        "The file must be present after the task."
    )


def test_retention_toml_exists():
    assert os.path.isfile(RETENTION_TOML_PATH), (
        f"File '{RETENTION_TOML_PATH}' does not exist. "
        "The file must be present after the task."
    )


# ── Exact content checks ──────────────────────────────────────────────────────

def test_backup_config_yaml_exact_content():
    with open(BACKUP_CONFIG_PATH, "r") as f:
        content = f.read().rstrip("\n")
    assert content == EXPECTED_BACKUP_CONFIG, (
        f"File '{BACKUP_CONFIG_PATH}' does not match the expected final content.\n"
        f"Expected:\n{EXPECTED_BACKUP_CONFIG}\n\n"
        f"Actual:\n{content}"
    )


def test_retention_toml_exact_content():
    with open(RETENTION_TOML_PATH, "r") as f:
        content = f.read().rstrip("\n")
    assert content == EXPECTED_RETENTION_TOML, (
        f"File '{RETENTION_TOML_PATH}' does not match the expected final content.\n"
        f"Expected:\n{EXPECTED_RETENTION_TOML}\n\n"
        f"Actual:\n{content}"
    )


# ── Individual field checks for backup_config.yaml ───────────────────────────

def test_backup_config_retention_days_is_30():
    with open(BACKUP_CONFIG_PATH, "r") as f:
        content = f.read()
    assert "retention_days: 30" in content, (
        f"Expected 'retention_days: 30' in '{BACKUP_CONFIG_PATH}', "
        f"but it was not found.\nCurrent content:\n{content}"
    )


def test_backup_config_retention_days_not_old_value():
    with open(BACKUP_CONFIG_PATH, "r") as f:
        content = f.read()
    assert "retention_days: 7" not in content, (
        f"Old value 'retention_days: 7' still present in '{BACKUP_CONFIG_PATH}'. "
        f"It should have been updated to 30.\nCurrent content:\n{content}"
    )


def test_backup_config_schedule_is_0_2():
    with open(BACKUP_CONFIG_PATH, "r") as f:
        content = f.read()
    assert 'schedule: "0 2 * * *"' in content, (
        f"Expected 'schedule: \"0 2 * * *\"' in '{BACKUP_CONFIG_PATH}', "
        f"but it was not found.\nCurrent content:\n{content}"
    )


def test_backup_config_schedule_not_old_value():
    with open(BACKUP_CONFIG_PATH, "r") as f:
        content = f.read()
    assert 'schedule: "0 3 * * *"' not in content, (
        f"Old value 'schedule: \"0 3 * * *\"' still present in '{BACKUP_CONFIG_PATH}'. "
        f"It should have been updated to '0 2 * * *'.\nCurrent content:\n{content}"
    )


def test_backup_config_bucket_is_prod_v2():
    with open(BACKUP_CONFIG_PATH, "r") as f:
        content = f.read()
    assert "bucket: db-backups-prod-v2" in content, (
        f"Expected 'bucket: db-backups-prod-v2' in '{BACKUP_CONFIG_PATH}', "
        f"but it was not found.\nCurrent content:\n{content}"
    )


def test_backup_config_bucket_not_old_value():
    with open(BACKUP_CONFIG_PATH, "r") as f:
        content = f.read()
    assert "bucket: db-backups-staging" not in content, (
        f"Old value 'bucket: db-backups-staging' still present in '{BACKUP_CONFIG_PATH}'. "
        f"It should have been updated to 'db-backups-prod-v2'.\nCurrent content:\n{content}"
    )


def test_backup_config_region_is_us_east_2():
    with open(BACKUP_CONFIG_PATH, "r") as f:
        content = f.read()
    assert "region: us-east-2" in content, (
        f"Expected 'region: us-east-2' in '{BACKUP_CONFIG_PATH}', "
        f"but it was not found.\nCurrent content:\n{content}"
    )


def test_backup_config_region_not_old_value():
    with open(BACKUP_CONFIG_PATH, "r") as f:
        content = f.read()
    assert "region: us-west-2" not in content, (
        f"Old value 'region: us-west-2' still present in '{BACKUP_CONFIG_PATH}'. "
        f"It should have been updated to 'us-east-2'.\nCurrent content:\n{content}"
    )


# ── Unchanged fields still present in backup_config.yaml ─────────────────────

def test_backup_config_database_section_preserved():
    with open(BACKUP_CONFIG_PATH, "r") as f:
        content = f.read()
    assert "host: postgres-primary.internal" in content, (
        f"'host: postgres-primary.internal' missing from '{BACKUP_CONFIG_PATH}'. "
        "This field should not have been changed."
    )
    assert "port: 5432" in content, (
        f"'port: 5432' missing from '{BACKUP_CONFIG_PATH}'. "
        "This field should not have been changed."
    )
    assert "name: appdb" in content, (
        f"'name: appdb' missing from '{BACKUP_CONFIG_PATH}'. "
        "This field should not have been changed."
    )


def test_backup_config_encryption_preserved():
    with open(BACKUP_CONFIG_PATH, "r") as f:
        content = f.read()
    assert "encryption: true" in content, (
        f"'encryption: true' missing from '{BACKUP_CONFIG_PATH}'. "
        "This field should not have been changed."
    )


def test_backup_config_notifications_preserved():
    with open(BACKUP_CONFIG_PATH, "r") as f:
        content = f.read()
    assert "email: dba-team@company.com" in content, (
        f"'email: dba-team@company.com' missing from '{BACKUP_CONFIG_PATH}'. "
        "This field should not have been changed."
    )
    assert "on_failure: true" in content, (
        f"'on_failure: true' missing from '{BACKUP_CONFIG_PATH}'. "
        "This field should not have been changed."
    )


# ── Individual field checks for retention.toml ────────────────────────────────

def test_retention_toml_enabled_is_true():
    with open(RETENTION_TOML_PATH, "r") as f:
        content = f.read()
    assert "enabled = true" in content, (
        f"Expected 'enabled = true' in '{RETENTION_TOML_PATH}', "
        f"but it was not found.\nCurrent content:\n{content}"
    )


def test_retention_toml_enabled_not_false():
    with open(RETENTION_TOML_PATH, "r") as f:
        content = f.read()
    assert "enabled = false" not in content, (
        f"Old value 'enabled = false' still present in '{RETENTION_TOML_PATH}'. "
        f"It should have been updated to true.\nCurrent content:\n{content}"
    )


def test_retention_toml_daily_keep_days_is_14():
    with open(RETENTION_TOML_PATH, "r") as f:
        content = f.read()
    assert "keep_days = 14" in content, (
        f"Expected 'keep_days = 14' (daily policy) in '{RETENTION_TOML_PATH}', "
        f"but it was not found.\nCurrent content:\n{content}"
    )


def test_retention_toml_weekly_keep_days_is_60():
    with open(RETENTION_TOML_PATH, "r") as f:
        content = f.read()
    assert "keep_days = 60" in content, (
        f"Expected 'keep_days = 60' (weekly policy) in '{RETENTION_TOML_PATH}', "
        f"but it was not found.\nCurrent content:\n{content}"
    )


def test_retention_toml_monthly_keep_days_is_365():
    with open(RETENTION_TOML_PATH, "r") as f:
        content = f.read()
    assert "keep_days = 365" in content, (
        f"Expected 'keep_days = 365' (monthly policy) in '{RETENTION_TOML_PATH}', "
        f"but it was not found.\nCurrent content:\n{content}"
    )


def test_retention_toml_old_daily_keep_days_not_present():
    with open(RETENTION_TOML_PATH, "r") as f:
        content = f.read()
    assert "keep_days = 7" not in content, (
        f"Old value 'keep_days = 7' still present in '{RETENTION_TOML_PATH}'. "
        f"It should have been updated to 14.\nCurrent content:\n{content}"
    )


def test_retention_toml_old_weekly_keep_days_not_present():
    with open(RETENTION_TOML_PATH, "r") as f:
        content = f.read()
    assert "keep_days = 30" not in content, (
        f"Old value 'keep_days = 30' still present in '{RETENTION_TOML_PATH}'. "
        f"It should have been updated to 60.\nCurrent content:\n{content}"
    )


def test_retention_toml_old_monthly_keep_days_not_present():
    with open(RETENTION_TOML_PATH, "r") as f:
        content = f.read()
    assert "keep_days = 180" not in content, (
        f"Old value 'keep_days = 180' still present in '{RETENTION_TOML_PATH}'. "
        f"It should have been updated to 365.\nCurrent content:\n{content}"
    )


# ── Unchanged fields still present in retention.toml ─────────────────────────

def test_retention_toml_version_preserved():
    with open(RETENTION_TOML_PATH, "r") as f:
        content = f.read()
    assert 'version = "2.0"' in content, (
        f"'version = \"2.0\"' missing from '{RETENTION_TOML_PATH}'. "
        "This field should not have been changed."
    )


def test_retention_toml_compress_settings_preserved():
    with open(RETENTION_TOML_PATH, "r") as f:
        content = f.read()
    # daily and weekly compress = true, monthly compress = false
    assert content.count("compress = true") == 2, (
        f"Expected exactly 2 occurrences of 'compress = true' in '{RETENTION_TOML_PATH}'. "
        f"Current content:\n{content}"
    )
    assert "compress = false" in content, (
        f"'compress = false' missing from '{RETENTION_TOML_PATH}'. "
        "This field should not have been changed."
    )


def test_retention_toml_section_headers_preserved():
    with open(RETENTION_TOML_PATH, "r") as f:
        content = f.read()
    for header in ("[policy.daily]", "[policy.weekly]", "[policy.monthly]"):
        assert header in content, (
            f"Section header '{header}' missing from '{RETENTION_TOML_PATH}'. "
            "This should not have been removed."
        )


# ── Readability ───────────────────────────────────────────────────────────────

def test_backup_config_yaml_is_readable():
    assert os.access(BACKUP_CONFIG_PATH, os.R_OK), (
        f"File '{BACKUP_CONFIG_PATH}' is not readable."
    )


def test_retention_toml_is_readable():
    assert os.access(RETENTION_TOML_PATH, os.R_OK), (
        f"File '{RETENTION_TOML_PATH}' is not readable."
    )