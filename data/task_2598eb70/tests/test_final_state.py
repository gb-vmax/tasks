# test_final_state.py

import os
import pytest

YAML_PATH = "/home/user/services/gateway/config.yaml"
TOML_PATH = "/home/user/services/broker/config.toml"

EXPECTED_YAML_CONTENT = """\
service:
  name: api-gateway
  replicas: 4
  image:
    repository: myregistry/api-gateway
    tag: v2.5.1
  resources:
    limits:
      memory: 1024Mi
      cpu: "500m"
    requests:
      memory: 256Mi
      cpu: "250m"
  port: 8080
  env: production"""

EXPECTED_TOML_CONTENT = """\
[service]
name = "message-broker"
version = "1.3.0"
env = "production"

[pool]
max_connections = 200
min_connections = 5
timeout_seconds = 30
idle_timeout = 300

[telemetry]
enabled = true
endpoint = "http://metrics.internal:9090"
interval_seconds = 15"""


# ---------------------------------------------------------------------------
# File existence / readability
# ---------------------------------------------------------------------------

def test_yaml_file_exists():
    assert os.path.isfile(YAML_PATH), (
        f"YAML config file not found at: {YAML_PATH}"
    )


def test_toml_file_exists():
    assert os.path.isfile(TOML_PATH), (
        f"TOML config file not found at: {TOML_PATH}"
    )


def test_yaml_file_is_readable():
    assert os.access(YAML_PATH, os.R_OK), (
        f"YAML config file is not readable: {YAML_PATH}"
    )


def test_toml_file_is_readable():
    assert os.access(TOML_PATH, os.R_OK), (
        f"TOML config file is not readable: {TOML_PATH}"
    )


# ---------------------------------------------------------------------------
# Full-content assertions (most authoritative)
# ---------------------------------------------------------------------------

def test_yaml_final_content():
    with open(YAML_PATH, "r") as f:
        content = f.read().rstrip("\n")
    assert content == EXPECTED_YAML_CONTENT, (
        f"config.yaml content does not match the expected final state.\n"
        f"Expected:\n{EXPECTED_YAML_CONTENT}\n\n"
        f"Actual:\n{content}"
    )


def test_toml_final_content():
    with open(TOML_PATH, "r") as f:
        content = f.read().rstrip("\n")
    assert content == EXPECTED_TOML_CONTENT, (
        f"config.toml content does not match the expected final state.\n"
        f"Expected:\n{EXPECTED_TOML_CONTENT}\n\n"
        f"Actual:\n{content}"
    )


# ---------------------------------------------------------------------------
# Targeted line-level assertions for config.yaml
# ---------------------------------------------------------------------------

def test_yaml_replicas_is_4():
    with open(YAML_PATH, "r") as f:
        lines = f.readlines()
    replicas_lines = [l for l in lines if "replicas" in l]
    assert replicas_lines, f"No 'replicas' line found in {YAML_PATH}"
    line = replicas_lines[0].rstrip("\n")
    assert line == "  replicas: 4", (
        f"Expected '  replicas: 4' but got: '{line}'. "
        f"The replicas value must be updated to 4."
    )


def test_yaml_memory_limit_is_1024Mi():
    with open(YAML_PATH, "r") as f:
        lines = f.readlines()
    in_limits = False
    found = False
    for line in lines:
        stripped = line.rstrip("\n")
        if "limits:" in stripped:
            in_limits = True
            continue
        if in_limits and "memory:" in stripped:
            assert stripped == "      memory: 1024Mi", (
                f"Expected '      memory: 1024Mi' under resources.limits but got: '{stripped}'. "
                f"The memory limit must be updated to 1024Mi."
            )
            found = True
            break
        # Stop looking once we leave the limits block (dedent or new key at same/higher level)
        if in_limits and stripped and not stripped.startswith("      "):
            break
    assert found, (
        f"Could not find the 'memory' line under the 'limits' section in {YAML_PATH}."
    )


def test_yaml_tag_is_v2_5_1():
    with open(YAML_PATH, "r") as f:
        lines = f.readlines()
    tag_lines = [l.rstrip("\n") for l in lines if "tag:" in l]
    assert tag_lines, f"No 'tag' line found in {YAML_PATH}"
    assert tag_lines[0] == "    tag: v2.5.1", (
        f"Expected '    tag: v2.5.1' but got: '{tag_lines[0]}'. "
        f"The image tag must be updated to v2.5.1."
    )


def test_yaml_unchanged_fields():
    """Verify that fields not targeted for change remain intact."""
    with open(YAML_PATH, "r") as f:
        content = f.read()

    checks = {
        "service name":        ("  name: api-gateway",         "  name: api-gateway"),
        "image repository":    ("    repository: myregistry/api-gateway",
                                "    repository: myregistry/api-gateway"),
        "cpu limit":           ('      cpu: "500m"',            '      cpu: "500m"'),
        "requests memory":     ("      memory: 256Mi",          "requests memory 256Mi"),
        "requests cpu":        ('      cpu: "250m"',            '      cpu: "250m"'),
        "port":                ("  port: 8080",                 "  port: 8080"),
        "env":                 ("  env: production",            "  env: production"),
    }

    lines = content.splitlines()

    # Check service name
    assert any(l == "  name: api-gateway" for l in lines), (
        "Field 'service.name' should remain 'api-gateway' but it appears to have changed."
    )
    # Check image repository
    assert any(l == "    repository: myregistry/api-gateway" for l in lines), (
        "Field 'image.repository' should remain 'myregistry/api-gateway' but it appears to have changed."
    )
    # Check cpu limit
    assert any(l == '      cpu: "500m"' for l in lines), (
        "Field 'resources.limits.cpu' should remain '\"500m\"' but it appears to have changed."
    )
    # Check port
    assert any(l == "  port: 8080" for l in lines), (
        "Field 'port' should remain 8080 but it appears to have changed."
    )
    # Check env
    assert any(l == "  env: production" for l in lines), (
        "Field 'env' should remain 'production' but it appears to have changed."
    )

    # requests section: memory 256Mi must appear (it's in requests, not limits)
    # We need to confirm it's still there (not deduplicated away)
    memory_lines = [l for l in lines if "memory:" in l]
    assert len(memory_lines) == 2, (
        f"Expected exactly 2 'memory:' lines (one in limits, one in requests), "
        f"found {len(memory_lines)}: {memory_lines}"
    )
    memory_values = {l.strip() for l in memory_lines}
    assert "memory: 1024Mi" in memory_values, (
        "limits memory (1024Mi) line is missing."
    )
    assert "memory: 256Mi" in memory_values, (
        "requests memory (256Mi) line should remain unchanged but appears to be missing."
    )


# ---------------------------------------------------------------------------
# Targeted line-level assertions for config.toml
# ---------------------------------------------------------------------------

def test_toml_max_connections_is_200():
    with open(TOML_PATH, "r") as f:
        lines = f.readlines()
    mc_lines = [l.rstrip("\n") for l in lines if "max_connections" in l]
    assert mc_lines, f"No 'max_connections' line found in {TOML_PATH}"
    assert mc_lines[0] == "max_connections = 200", (
        f"Expected 'max_connections = 200' but got: '{mc_lines[0]}'. "
        f"max_connections under [pool] must be updated to 200."
    )


def test_toml_timeout_seconds_is_30():
    with open(TOML_PATH, "r") as f:
        lines = f.readlines()
    ts_lines = [l.rstrip("\n") for l in lines if "timeout_seconds" in l]
    assert ts_lines, f"No 'timeout_seconds' line found in {TOML_PATH}"
    assert ts_lines[0] == "timeout_seconds = 30", (
        f"Expected 'timeout_seconds = 30' but got: '{ts_lines[0]}'. "
        f"timeout_seconds under [pool] must be updated to 30."
    )


def test_toml_telemetry_enabled_is_true():
    with open(TOML_PATH, "r") as f:
        lines = f.readlines()
    enabled_lines = [l.rstrip("\n") for l in lines if l.strip().startswith("enabled")]
    assert enabled_lines, f"No 'enabled' line found in {TOML_PATH}"
    assert enabled_lines[0] == "enabled = true", (
        f"Expected 'enabled = true' but got: '{enabled_lines[0]}'. "
        f"telemetry.enabled must be updated to true."
    )


def test_toml_unchanged_fields():
    """Verify that fields not targeted for change remain intact."""
    with open(TOML_PATH, "r") as f:
        lines = [l.rstrip("\n") for l in f.readlines()]

    expected_unchanged = [
        '[service]',
        'name = "message-broker"',
        'version = "1.3.0"',
        'env = "production"',
        '[pool]',
        'min_connections = 5',
        'idle_timeout = 300',
        '[telemetry]',
        'endpoint = "http://metrics.internal:9090"',
        'interval_seconds = 15',
    ]

    for expected_line in expected_unchanged:
        assert expected_line in lines, (
            f"Expected line '{expected_line}' is missing or was incorrectly modified in {TOML_PATH}. "
            f"Only the specified fields should have been changed."
        )


# ---------------------------------------------------------------------------
# Structural / section integrity
# ---------------------------------------------------------------------------

def test_yaml_has_all_required_sections():
    with open(YAML_PATH, "r") as f:
        content = f.read()
    required_keys = ["service:", "image:", "resources:", "limits:", "requests:"]
    for key in required_keys:
        assert key in content, (
            f"Required YAML key/section '{key}' is missing from {YAML_PATH}. "
            f"The file structure may have been mangled."
        )


def test_toml_has_all_required_sections():
    with open(TOML_PATH, "r") as f:
        content = f.read()
    required_sections = ["[service]", "[pool]", "[telemetry]"]
    for section in required_sections:
        assert section in content, (
            f"Required TOML section '{section}' is missing from {TOML_PATH}. "
            f"The file structure may have been mangled."
        )


def test_yaml_line_count():
    with open(YAML_PATH, "r") as f:
        lines = [l for l in f.readlines() if l.rstrip("\n")]  # non-empty lines
    expected_lines = EXPECTED_YAML_CONTENT.splitlines()
    assert len(lines) == len(expected_lines), (
        f"config.yaml has {len(lines)} non-empty lines but expected {len(expected_lines)}. "
        f"Lines may have been added or removed unintentionally."
    )


def test_toml_line_count():
    with open(TOML_PATH, "r") as f:
        content = f.read().rstrip("\n")
    actual_lines = content.splitlines()
    expected_lines = EXPECTED_TOML_CONTENT.splitlines()
    assert len(actual_lines) == len(expected_lines), (
        f"config.toml has {len(actual_lines)} lines but expected {len(expected_lines)}. "
        f"Lines may have been added or removed unintentionally."
    )