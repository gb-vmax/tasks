# test_final_state.py

import os
import pytest

BASE = "/home/user/finops/reports"
DIR_2024_06 = os.path.join(BASE, "2024-06")
DIR_CURRENT = os.path.join(BASE, "current")

AWS_LINK = os.path.join(DIR_CURRENT, "aws.csv")
GCP_LINK = os.path.join(DIR_CURRENT, "gcp.csv")
AZURE_LINK = os.path.join(DIR_CURRENT, "azure.csv")
SUMMARY_FILE = os.path.join(DIR_CURRENT, "links_summary.txt")

AWS_TARGET = os.path.join(DIR_2024_06, "aws_costs_2024-06.csv")
GCP_TARGET = os.path.join(DIR_2024_06, "gcp_costs_2024-06.csv")
AZURE_TARGET = os.path.join(DIR_2024_06, "azure_costs_2024-06.csv")

AWS_CONTENT = "service,cost_usd\nEC2,1200.50\nS3,340.20\nRDS,890.00"
GCP_CONTENT = "service,cost_usd\nCompute Engine,980.75\nCloud Storage,210.40\nBigQuery,560.10"
AZURE_CONTENT = "service,cost_usd\nVirtual Machines,1050.30\nBlob Storage,175.60\nAzure SQL,720.90"

EXPECTED_SUMMARY = (
    "aws.csv -> /home/user/finops/reports/2024-06/aws_costs_2024-06.csv\n"
    "azure.csv -> /home/user/finops/reports/2024-06/azure_costs_2024-06.csv\n"
    "gcp.csv -> /home/user/finops/reports/2024-06/gcp_costs_2024-06.csv\n"
)


# --- Symlink existence and type checks ---

def test_aws_symlink_exists():
    assert os.path.exists(AWS_LINK) or os.path.islink(AWS_LINK), (
        f"{AWS_LINK} does not exist. The symlink was not created."
    )


def test_gcp_symlink_exists():
    assert os.path.exists(GCP_LINK) or os.path.islink(GCP_LINK), (
        f"{GCP_LINK} does not exist. The symlink was not created."
    )


def test_azure_symlink_exists():
    assert os.path.exists(AZURE_LINK) or os.path.islink(AZURE_LINK), (
        f"{AZURE_LINK} does not exist. The symlink was not created."
    )


def test_aws_is_symlink():
    assert os.path.islink(AWS_LINK), (
        f"{AWS_LINK} exists but is NOT a symbolic link. It must be a symlink, not a copy."
    )


def test_gcp_is_symlink():
    assert os.path.islink(GCP_LINK), (
        f"{GCP_LINK} exists but is NOT a symbolic link. It must be a symlink, not a copy."
    )


def test_azure_is_symlink():
    assert os.path.islink(AZURE_LINK), (
        f"{AZURE_LINK} exists but is NOT a symbolic link. It must be a symlink, not a copy."
    )


# --- Symlink target checks (readlink) ---

def test_aws_symlink_target():
    target = os.readlink(AWS_LINK)
    assert target == AWS_TARGET, (
        f"Symlink {AWS_LINK} points to wrong target.\n"
        f"Expected: {AWS_TARGET}\n"
        f"Got:      {target}"
    )


def test_gcp_symlink_target():
    target = os.readlink(GCP_LINK)
    assert target == GCP_TARGET, (
        f"Symlink {GCP_LINK} points to wrong target.\n"
        f"Expected: {GCP_TARGET}\n"
        f"Got:      {target}"
    )


def test_azure_symlink_target():
    target = os.readlink(AZURE_LINK)
    assert target == AZURE_TARGET, (
        f"Symlink {AZURE_LINK} points to wrong target.\n"
        f"Expected: {AZURE_TARGET}\n"
        f"Got:      {target}"
    )


# --- Symlink resolution (reading through the symlink returns correct content) ---

def test_aws_symlink_resolves_correctly():
    assert os.path.isfile(AWS_LINK), (
        f"Symlink {AWS_LINK} does not resolve to an existing file. "
        f"The target {AWS_TARGET} may be missing or the symlink is broken."
    )
    with open(AWS_LINK, "r") as f:
        content = f.read().strip()
    assert content == AWS_CONTENT, (
        f"Reading through symlink {AWS_LINK} returned unexpected content.\n"
        f"Expected:\n{AWS_CONTENT}\n\nGot:\n{content}"
    )


def test_gcp_symlink_resolves_correctly():
    assert os.path.isfile(GCP_LINK), (
        f"Symlink {GCP_LINK} does not resolve to an existing file. "
        f"The target {GCP_TARGET} may be missing or the symlink is broken."
    )
    with open(GCP_LINK, "r") as f:
        content = f.read().strip()
    assert content == GCP_CONTENT, (
        f"Reading through symlink {GCP_LINK} returned unexpected content.\n"
        f"Expected:\n{GCP_CONTENT}\n\nGot:\n{content}"
    )


def test_azure_symlink_resolves_correctly():
    assert os.path.isfile(AZURE_LINK), (
        f"Symlink {AZURE_LINK} does not resolve to an existing file. "
        f"The target {AZURE_TARGET} may be missing or the symlink is broken."
    )
    with open(AZURE_LINK, "r") as f:
        content = f.read().strip()
    assert content == AZURE_CONTENT, (
        f"Reading through symlink {AZURE_LINK} returned unexpected content.\n"
        f"Expected:\n{AZURE_CONTENT}\n\nGot:\n{content}"
    )


# --- links_summary.txt checks ---

def test_links_summary_exists():
    assert os.path.exists(SUMMARY_FILE), (
        f"{SUMMARY_FILE} does not exist. The summary file was not created."
    )


def test_links_summary_is_regular_file():
    assert os.path.isfile(SUMMARY_FILE), (
        f"{SUMMARY_FILE} exists but is not a regular file."
    )


def test_links_summary_line_count():
    with open(SUMMARY_FILE, "r") as f:
        content = f.read()
    lines = content.splitlines()
    assert len(lines) == 3, (
        f"{SUMMARY_FILE} should contain exactly 3 lines, but found {len(lines)}.\n"
        f"Content:\n{content!r}"
    )


def test_links_summary_exact_content():
    with open(SUMMARY_FILE, "r") as f:
        content = f.read()
    assert content == EXPECTED_SUMMARY, (
        f"Content of {SUMMARY_FILE} does not match expected.\n"
        f"Expected (repr): {EXPECTED_SUMMARY!r}\n"
        f"Got (repr):      {content!r}"
    )


def test_links_summary_no_trailing_spaces():
    with open(SUMMARY_FILE, "r") as f:
        content = f.read()
    lines = content.splitlines()
    for i, line in enumerate(lines, start=1):
        assert line == line.rstrip(), (
            f"Line {i} in {SUMMARY_FILE} has trailing whitespace: {line!r}"
        )


def test_links_summary_no_blank_lines():
    with open(SUMMARY_FILE, "r") as f:
        content = f.read()
    lines = content.splitlines()
    for i, line in enumerate(lines, start=1):
        assert line.strip() != "", (
            f"Line {i} in {SUMMARY_FILE} is blank or whitespace-only."
        )


def test_links_summary_alphabetical_order():
    with open(SUMMARY_FILE, "r") as f:
        content = f.read()
    lines = content.splitlines()
    assert len(lines) == 3, (
        f"Expected 3 lines in {SUMMARY_FILE}, got {len(lines)}."
    )
    expected_order = [
        f"aws.csv -> {AWS_TARGET}",
        f"azure.csv -> {AZURE_TARGET}",
        f"gcp.csv -> {GCP_TARGET}",
    ]
    for i, (actual, expected) in enumerate(zip(lines, expected_order), start=1):
        assert actual == expected, (
            f"Line {i} in {SUMMARY_FILE} is incorrect.\n"
            f"Expected: {expected!r}\n"
            f"Got:      {actual!r}"
        )


def test_links_summary_arrow_format():
    """Each line must use exactly ' -> ' (space-arrow-space) as separator."""
    with open(SUMMARY_FILE, "r") as f:
        content = f.read()
    lines = content.splitlines()
    for i, line in enumerate(lines, start=1):
        assert " -> " in line, (
            f"Line {i} in {SUMMARY_FILE} does not contain ' -> ' separator: {line!r}"
        )
        parts = line.split(" -> ")
        assert len(parts) == 2, (
            f"Line {i} in {SUMMARY_FILE} has unexpected format (more than one ' -> '): {line!r}"
        )
        link_name, target_path = parts
        assert link_name == link_name.strip(), (
            f"Line {i} in {SUMMARY_FILE}: link name has unexpected whitespace: {link_name!r}"
        )
        assert target_path == target_path.strip(), (
            f"Line {i} in {SUMMARY_FILE}: target path has unexpected whitespace: {target_path!r}"
        )