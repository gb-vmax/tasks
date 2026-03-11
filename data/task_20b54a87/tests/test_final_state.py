# test_final_state.py

import os
import pytest

YAML_PATH = "/home/user/mlops/experiments/run_42.yaml"
TOML_PATH = "/home/user/mlops/artifacts/registry.toml"

EXPECTED_YAML_CONTENT = '''\
experiment_name: gradient_boost_experiment
run_id: 42
status: "completed"
model:
  type: gradient_boosting
  n_estimators: 200
  learning_rate: 0.05
  max_depth: 5
metrics:
  val_accuracy: 0.9173
  val_loss: 0.2041
  train_accuracy: 0.9512
artifact_path: "s3://mlops-bucket/run_42/model.pkl"'''

EXPECTED_TOML_CONTENT = '''\
[[models]]
run_id = 39
name = "gradient_boost_v1"
status = "production"
val_accuracy = 0.8841
artifact_path = "s3://mlops-bucket/run_39/model.pkl"

[[models]]
run_id = 41
name = "gradient_boost_v2"
status = "archived"
val_accuracy = 0.9005
artifact_path = "s3://mlops-bucket/run_41/model.pkl"

[[models]]
run_id = 42
name = "gradient_boost_v3"
status = "staged"
val_accuracy = 0.9173
artifact_path = "s3://mlops-bucket/run_42/model.pkl"'''


# ---------------------------------------------------------------------------
# Directory / file existence checks
# ---------------------------------------------------------------------------

def test_mlops_directory_exists():
    assert os.path.isdir("/home/user/mlops"), (
        "Expected directory /home/user/mlops does not exist."
    )


def test_experiments_directory_exists():
    assert os.path.isdir("/home/user/mlops/experiments"), (
        "Expected directory /home/user/mlops/experiments does not exist."
    )


def test_artifacts_directory_exists():
    assert os.path.isdir("/home/user/mlops/artifacts"), (
        "Expected directory /home/user/mlops/artifacts does not exist."
    )


def test_yaml_file_exists():
    assert os.path.isfile(YAML_PATH), (
        f"Expected file does not exist: {YAML_PATH}"
    )


def test_yaml_file_is_readable():
    assert os.access(YAML_PATH, os.R_OK), (
        f"File is not readable: {YAML_PATH}"
    )


def test_toml_file_exists():
    assert os.path.isfile(TOML_PATH), (
        f"Expected file does not exist: {TOML_PATH}"
    )


def test_toml_file_is_readable():
    assert os.access(TOML_PATH, os.R_OK), (
        f"File is not readable: {TOML_PATH}"
    )


# ---------------------------------------------------------------------------
# YAML final-state checks
# ---------------------------------------------------------------------------

def test_yaml_full_content():
    with open(YAML_PATH, "r") as f:
        content = f.read().rstrip("\n")
    assert content == EXPECTED_YAML_CONTENT, (
        f"Content of {YAML_PATH} does not match expected final state.\n"
        f"Expected:\n{EXPECTED_YAML_CONTENT}\n\nActual:\n{content}"
    )


def test_yaml_status_is_completed():
    with open(YAML_PATH, "r") as f:
        lines = f.readlines()
    status_lines = [l.rstrip("\n") for l in lines if l.strip().startswith("status:")]
    assert len(status_lines) == 1, (
        f"Expected exactly one 'status:' line in {YAML_PATH}, found: {status_lines}"
    )
    assert status_lines[0] == 'status: "completed"', (
        f"Expected status line to be 'status: \"completed\"', got: {status_lines[0]!r}"
    )


def test_yaml_val_accuracy_updated():
    with open(YAML_PATH, "r") as f:
        lines = f.readlines()
    val_acc_lines = [l.rstrip("\n") for l in lines if "val_accuracy" in l]
    assert len(val_acc_lines) == 1, (
        f"Expected exactly one 'val_accuracy' line in {YAML_PATH}, found: {val_acc_lines}"
    )
    assert val_acc_lines[0] == "  val_accuracy: 0.9173", (
        f"Expected '  val_accuracy: 0.9173', got: {val_acc_lines[0]!r}"
    )


def test_yaml_val_loss_updated():
    with open(YAML_PATH, "r") as f:
        lines = f.readlines()
    val_loss_lines = [l.rstrip("\n") for l in lines if "val_loss" in l]
    assert len(val_loss_lines) == 1, (
        f"Expected exactly one 'val_loss' line in {YAML_PATH}, found: {val_loss_lines}"
    )
    assert val_loss_lines[0] == "  val_loss: 0.2041", (
        f"Expected '  val_loss: 0.2041', got: {val_loss_lines[0]!r}"
    )


def test_yaml_artifact_path_present():
    with open(YAML_PATH, "r") as f:
        lines = f.readlines()
    artifact_lines = [l.rstrip("\n") for l in lines if l.strip().startswith("artifact_path:")]
    assert len(artifact_lines) == 1, (
        f"Expected exactly one top-level 'artifact_path:' line in {YAML_PATH}, "
        f"found: {artifact_lines}"
    )
    assert artifact_lines[0] == 'artifact_path: "s3://mlops-bucket/run_42/model.pkl"', (
        f"Expected artifact_path line to be "
        f"'artifact_path: \"s3://mlops-bucket/run_42/model.pkl\"', "
        f"got: {artifact_lines[0]!r}"
    )


def test_yaml_train_accuracy_unchanged():
    with open(YAML_PATH, "r") as f:
        lines = f.readlines()
    train_acc_lines = [l.rstrip("\n") for l in lines if "train_accuracy" in l]
    assert len(train_acc_lines) == 1, (
        f"Expected exactly one 'train_accuracy' line in {YAML_PATH}, found: {train_acc_lines}"
    )
    assert train_acc_lines[0] == "  train_accuracy: 0.9512", (
        f"Expected '  train_accuracy: 0.9512', got: {train_acc_lines[0]!r}"
    )


def test_yaml_status_not_running():
    with open(YAML_PATH, "r") as f:
        content = f.read()
    assert 'status: "running"' not in content, (
        f"Found 'status: \"running\"' in {YAML_PATH} — status was not updated to 'completed'."
    )


def test_yaml_val_accuracy_not_null():
    with open(YAML_PATH, "r") as f:
        content = f.read()
    assert "val_accuracy: null" not in content, (
        f"Found 'val_accuracy: null' in {YAML_PATH} — val_accuracy was not updated."
    )


def test_yaml_val_loss_not_null():
    with open(YAML_PATH, "r") as f:
        content = f.read()
    assert "val_loss: null" not in content, (
        f"Found 'val_loss: null' in {YAML_PATH} — val_loss was not updated."
    )


# ---------------------------------------------------------------------------
# TOML final-state checks
# ---------------------------------------------------------------------------

def test_toml_full_content():
    with open(TOML_PATH, "r") as f:
        content = f.read().rstrip("\n")
    assert content == EXPECTED_TOML_CONTENT, (
        f"Content of {TOML_PATH} does not match expected final state.\n"
        f"Expected:\n{EXPECTED_TOML_CONTENT}\n\nActual:\n{content}"
    )


def test_toml_has_exactly_three_models():
    with open(TOML_PATH, "r") as f:
        content = f.read()
    count = content.count("[[models]]")
    assert count == 3, (
        f"Expected exactly 3 [[models]] sections in {TOML_PATH}, found: {count}"
    )


def test_toml_first_model_block_unchanged():
    with open(TOML_PATH, "r") as f:
        content = f.read()
    assert 'run_id = 39' in content, (
        f"Missing 'run_id = 39' in {TOML_PATH}"
    )
    assert 'name = "gradient_boost_v1"' in content, (
        f"Missing 'name = \"gradient_boost_v1\"' in {TOML_PATH}"
    )
    assert 'status = "production"' in content, (
        f"Missing 'status = \"production\"' in {TOML_PATH}"
    )
    assert 'val_accuracy = 0.8841' in content, (
        f"Missing 'val_accuracy = 0.8841' in {TOML_PATH}"
    )
    assert 'artifact_path = "s3://mlops-bucket/run_39/model.pkl"' in content, (
        f"Missing 'artifact_path = \"s3://mlops-bucket/run_39/model.pkl\"' in {TOML_PATH}"
    )


def test_toml_second_model_block_unchanged():
    with open(TOML_PATH, "r") as f:
        content = f.read()
    assert 'run_id = 41' in content, (
        f"Missing 'run_id = 41' in {TOML_PATH}"
    )
    assert 'name = "gradient_boost_v2"' in content, (
        f"Missing 'name = \"gradient_boost_v2\"' in {TOML_PATH}"
    )
    assert 'status = "archived"' in content, (
        f"Missing 'status = \"archived\"' in {TOML_PATH}"
    )
    assert 'val_accuracy = 0.9005' in content, (
        f"Missing 'val_accuracy = 0.9005' in {TOML_PATH}"
    )
    assert 'artifact_path = "s3://mlops-bucket/run_41/model.pkl"' in content, (
        f"Missing 'artifact_path = \"s3://mlops-bucket/run_41/model.pkl\"' in {TOML_PATH}"
    )


def test_toml_third_model_block_present():
    with open(TOML_PATH, "r") as f:
        content = f.read()
    assert 'run_id = 42' in content, (
        f"Missing 'run_id = 42' in {TOML_PATH} — new model entry not added."
    )
    assert 'name = "gradient_boost_v3"' in content, (
        f"Missing 'name = \"gradient_boost_v3\"' in {TOML_PATH}"
    )
    assert 'status = "staged"' in content, (
        f"Missing 'status = \"staged\"' in {TOML_PATH}"
    )
    assert 'val_accuracy = 0.9173' in content, (
        f"Missing 'val_accuracy = 0.9173' in {TOML_PATH}"
    )
    assert 'artifact_path = "s3://mlops-bucket/run_42/model.pkl"' in content, (
        f"Missing 'artifact_path = \"s3://mlops-bucket/run_42/model.pkl\"' in {TOML_PATH}"
    )


def test_toml_third_block_is_last():
    """Verify that the run_id=42 block appears after the run_id=41 block."""
    with open(TOML_PATH, "r") as f:
        content = f.read()
    pos_41 = content.find("run_id = 41")
    pos_42 = content.find("run_id = 42")
    assert pos_41 != -1, f"'run_id = 41' not found in {TOML_PATH}"
    assert pos_42 != -1, f"'run_id = 42' not found in {TOML_PATH}"
    assert pos_42 > pos_41, (
        f"Expected 'run_id = 42' block to appear after 'run_id = 41' block in {TOML_PATH}, "
        f"but positions were: run_id=41 at {pos_41}, run_id=42 at {pos_42}"
    )


def test_toml_third_block_field_order():
    """Verify the fields in the new [[models]] block appear in the required order."""
    with open(TOML_PATH, "r") as f:
        lines = f.readlines()

    # Find the index of the third [[models]] header
    models_indices = [i for i, l in enumerate(lines) if l.strip() == "[[models]]"]
    assert len(models_indices) == 3, (
        f"Expected 3 [[models]] headers, found {len(models_indices)} in {TOML_PATH}"
    )

    third_start = models_indices[2]
    block_lines = []
    for line in lines[third_start + 1:]:
        stripped = line.strip()
        if stripped == "" or stripped == "[[models]]":
            break
        block_lines.append(stripped)

    expected_fields_in_order = [
        "run_id = 42",
        'name = "gradient_boost_v3"',
        'status = "staged"',
        "val_accuracy = 0.9173",
        'artifact_path = "s3://mlops-bucket/run_42/model.pkl"',
    ]

    for expected in expected_fields_in_order:
        assert any(expected in bl for bl in block_lines), (
            f"Expected field '{expected}' not found in third [[models]] block of {TOML_PATH}. "
            f"Block lines: {block_lines}"
        )

    # Check ordering
    positions = []
    for expected in expected_fields_in_order:
        for idx, bl in enumerate(block_lines):
            if expected in bl:
                positions.append(idx)
                break

    assert positions == sorted(positions), (
        f"Fields in the third [[models]] block are not in the required order.\n"
        f"Expected order: {expected_fields_in_order}\n"
        f"Block lines: {block_lines}"
    )