# test_final_state.py

import os
import stat
import tarfile
import pytest

ARTIFACTS_DIR = "/home/user/artifacts"
BUILD_DIR = "/home/user/artifacts/build"
GZ_PATH = "/home/user/artifacts/build.tar.gz"
BZ2_PATH = "/home/user/artifacts/build.tar.bz2"
REPORT_PATH = "/home/user/artifacts/compression_report.txt"


# ---------------------------------------------------------------------------
# Archive existence tests
# ---------------------------------------------------------------------------

def test_gz_archive_exists():
    assert os.path.isfile(GZ_PATH), (
        f"gzip-compressed tarball does not exist: {GZ_PATH}"
    )


def test_bz2_archive_exists():
    assert os.path.isfile(BZ2_PATH), (
        f"bzip2-compressed tarball does not exist: {BZ2_PATH}"
    )


# ---------------------------------------------------------------------------
# Archive validity tests
# ---------------------------------------------------------------------------

def test_gz_archive_is_valid_tarball():
    assert os.path.isfile(GZ_PATH), f"File missing: {GZ_PATH}"
    try:
        with tarfile.open(GZ_PATH, "r:gz") as tf:
            members = tf.getnames()
    except Exception as e:
        pytest.fail(f"{GZ_PATH} is not a valid gzip tarball: {e}")
    assert len(members) > 0, f"{GZ_PATH} is an empty tarball"


def test_bz2_archive_is_valid_tarball():
    assert os.path.isfile(BZ2_PATH), f"File missing: {BZ2_PATH}"
    try:
        with tarfile.open(BZ2_PATH, "r:bz2") as tf:
            members = tf.getnames()
    except Exception as e:
        pytest.fail(f"{BZ2_PATH} is not a valid bzip2 tarball: {e}")
    assert len(members) > 0, f"{BZ2_PATH} is an empty tarball"


def test_gz_archive_contains_build_files():
    assert os.path.isfile(GZ_PATH), f"File missing: {GZ_PATH}"
    with tarfile.open(GZ_PATH, "r:gz") as tf:
        names = tf.getnames()
    # Normalise: strip leading './' or similar
    normalised = {n.lstrip("./") for n in names}
    expected_files = {"build/app.js", "build/styles.css", "build/manifest.json"}
    # Accept either "build/app.js" style or just "app.js" style
    flat_names = {os.path.basename(n) for n in normalised}
    assert "app.js" in flat_names, (
        f"app.js not found in {GZ_PATH}. Members: {names}"
    )
    assert "styles.css" in flat_names, (
        f"styles.css not found in {GZ_PATH}. Members: {names}"
    )
    assert "manifest.json" in flat_names, (
        f"manifest.json not found in {GZ_PATH}. Members: {names}"
    )


def test_bz2_archive_contains_build_files():
    assert os.path.isfile(BZ2_PATH), f"File missing: {BZ2_PATH}"
    with tarfile.open(BZ2_PATH, "r:bz2") as tf:
        names = tf.getnames()
    flat_names = {os.path.basename(n) for n in names}
    assert "app.js" in flat_names, (
        f"app.js not found in {BZ2_PATH}. Members: {names}"
    )
    assert "styles.css" in flat_names, (
        f"styles.css not found in {BZ2_PATH}. Members: {names}"
    )
    assert "manifest.json" in flat_names, (
        f"manifest.json not found in {BZ2_PATH}. Members: {names}"
    )


# ---------------------------------------------------------------------------
# Report existence test
# ---------------------------------------------------------------------------

def test_report_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Compression report does not exist: {REPORT_PATH}"
    )


# ---------------------------------------------------------------------------
# Report content tests
# ---------------------------------------------------------------------------

def _read_report_lines():
    """Return the lines of the report (stripped of trailing newline only)."""
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    # Split on newlines; the spec says exactly 4 newline-terminated lines
    lines = content.split("\n")
    # If the file ends with a newline the last element will be ''
    if lines and lines[-1] == "":
        lines = lines[:-1]
    return lines


def test_report_has_exactly_four_lines():
    lines = _read_report_lines()
    assert len(lines) == 4, (
        f"Expected exactly 4 lines in report, got {len(lines)}. "
        f"Content: {lines!r}"
    )


def test_report_line1_is_compression_comparison():
    lines = _read_report_lines()
    assert len(lines) >= 1, "Report has fewer than 1 line"
    assert lines[0] == "compression comparison", (
        f"Line 1 must be exactly 'compression comparison', got: {lines[0]!r}"
    )


def test_report_line2_gz_size_matches_actual():
    assert os.path.isfile(GZ_PATH), f"File missing: {GZ_PATH}"
    lines = _read_report_lines()
    assert len(lines) >= 2, "Report has fewer than 2 lines"

    line2 = lines[1]
    parts = line2.split(" ")
    assert len(parts) == 2, (
        f"Line 2 must be '<filename> <size>', got: {line2!r}"
    )
    filename, size_str = parts
    assert filename == "build.tar.gz", (
        f"Line 2 filename must be 'build.tar.gz', got: {filename!r}"
    )

    try:
        reported_size = int(size_str)
    except ValueError:
        pytest.fail(f"Line 2 size is not a valid integer: {size_str!r}")

    actual_size = os.stat(GZ_PATH).st_size
    assert reported_size == actual_size, (
        f"Line 2 reports size {reported_size} for build.tar.gz, "
        f"but actual file size is {actual_size} bytes. "
        f"The report is out of date or incorrect."
    )


def test_report_line3_bz2_size_matches_actual():
    assert os.path.isfile(BZ2_PATH), f"File missing: {BZ2_PATH}"
    lines = _read_report_lines()
    assert len(lines) >= 3, "Report has fewer than 3 lines"

    line3 = lines[2]
    parts = line3.split(" ")
    assert len(parts) == 2, (
        f"Line 3 must be '<filename> <size>', got: {line3!r}"
    )
    filename, size_str = parts
    assert filename == "build.tar.bz2", (
        f"Line 3 filename must be 'build.tar.bz2', got: {filename!r}"
    )

    try:
        reported_size = int(size_str)
    except ValueError:
        pytest.fail(f"Line 3 size is not a valid integer: {size_str!r}")

    actual_size = os.stat(BZ2_PATH).st_size
    assert reported_size == actual_size, (
        f"Line 3 reports size {reported_size} for build.tar.bz2, "
        f"but actual file size is {actual_size} bytes. "
        f"The report is out of date or incorrect."
    )


def test_report_line4_winner_is_correct():
    assert os.path.isfile(GZ_PATH), f"File missing: {GZ_PATH}"
    assert os.path.isfile(BZ2_PATH), f"File missing: {BZ2_PATH}"
    lines = _read_report_lines()
    assert len(lines) >= 4, "Report has fewer than 4 lines"

    gz_size = os.stat(GZ_PATH).st_size
    bz2_size = os.stat(BZ2_PATH).st_size

    if gz_size < bz2_size:
        expected_winner_line = "winner build.tar.gz"
    elif bz2_size < gz_size:
        expected_winner_line = "winner build.tar.bz2"
    else:
        expected_winner_line = "winner tie"

    assert lines[3] == expected_winner_line, (
        f"Line 4 should be {expected_winner_line!r} "
        f"(gz={gz_size} bytes, bz2={bz2_size} bytes), "
        f"but got: {lines[3]!r}"
    )


def test_report_no_trailing_spaces():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    lines = content.split("\n")
    # Drop final empty element if file ends with newline
    if lines and lines[-1] == "":
        lines = lines[:-1]
    for i, line in enumerate(lines, start=1):
        assert not line.endswith(" "), (
            f"Line {i} has trailing space(s): {line!r}"
        )


def test_report_no_extra_blank_lines():
    lines = _read_report_lines()
    for i, line in enumerate(lines, start=1):
        assert line != "", (
            f"Line {i} is blank; report must have no blank lines"
        )


def test_report_line2_no_commas_or_units():
    lines = _read_report_lines()
    assert len(lines) >= 2, "Report has fewer than 2 lines"
    size_str = lines[1].split(" ")[1] if " " in lines[1] else ""
    assert "," not in size_str, (
        f"Line 2 size must not contain commas: {size_str!r}"
    )
    # Should be purely numeric
    assert size_str.isdigit(), (
        f"Line 2 size must be a plain integer with no units: {size_str!r}"
    )


def test_report_line3_no_commas_or_units():
    lines = _read_report_lines()
    assert len(lines) >= 3, "Report has fewer than 3 lines"
    size_str = lines[2].split(" ")[1] if " " in lines[2] else ""
    assert "," not in size_str, (
        f"Line 3 size must not contain commas: {size_str!r}"
    )
    assert size_str.isdigit(), (
        f"Line 3 size must be a plain integer with no units: {size_str!r}"
    )


# ---------------------------------------------------------------------------
# Sanity: archives are non-zero size
# ---------------------------------------------------------------------------

def test_gz_archive_is_nonempty():
    assert os.path.isfile(GZ_PATH), f"File missing: {GZ_PATH}"
    size = os.stat(GZ_PATH).st_size
    assert size > 0, f"{GZ_PATH} is empty (0 bytes)"


def test_bz2_archive_is_nonempty():
    assert os.path.isfile(BZ2_PATH), f"File missing: {BZ2_PATH}"
    size = os.stat(BZ2_PATH).st_size
    assert size > 0, f"{BZ2_PATH} is empty (0 bytes)"