# test_final_state.py

import os
import pytest
import csv
import json

AUDIT_RUNS_CSV = '/home/user/audit_runs.csv'
AUDIT_RUNS_JSONL = '/home/user/audit_runs.jsonl'
AUDIT_SUMMARY_CSV = '/home/user/audit_summary.csv'
AUDIT_TASK_LOG = '/home/user/audit_task.log'

TRUTH_AUDIT_RUNS_CSV = (
    "run_id,pipeline,developer,start_time,status,duration_seconds\n"
    "1001,deploy-api,alice,2024-05-20T08:15:00Z,success,130\n"
    "1002,deploy-web,bob,2024-05-20T08:17:23Z,fail,95\n"
    "1003,deploy-api,charlie,2024-05-20T09:01:11Z,success,110\n"
)

TRUTH_AUDIT_RUNS_JSONL = [
    {
        "run_id": 1001,
        "pipeline": "deploy-api",
        "developer": "alice",
        "start_time": "2024-05-20T08:15:00Z",
        "status": "success",
        "duration_seconds": 130,
    },
    {
        "run_id": 1002,
        "pipeline": "deploy-web",
        "developer": "bob",
        "start_time": "2024-05-20T08:17:23Z",
        "status": "fail",
        "duration_seconds": 95,
    },
    {
        "run_id": 1003,
        "pipeline": "deploy-api",
        "developer": "charlie",
        "start_time": "2024-05-20T09:01:11Z",
        "status": "success",
        "duration_seconds": 110,
    },
]

TRUTH_AUDIT_SUMMARY_CSV = [
    ["pipeline", "total_runs", "success_count", "fail_count", "average_duration"],
    ["deploy-api", "2", "2", "0", "120"],
    ["deploy-web", "1", "0", "1", "95"],
]

TRUTH_AUDIT_TASK_LOG = [
    "JSONL generated: /home/user/audit_runs.jsonl\n",
    "Summary CSV generated: /home/user/audit_summary.csv\n",
]

@pytest.mark.describe("Final OS/Filesystem state validation after student action")
class TestFinalState:
    def test_audit_runs_csv_unchanged(self):
        """Check that /home/user/audit_runs.csv exists and is unchanged."""
        assert os.path.isfile(AUDIT_RUNS_CSV), (
            f"Missing input file: {AUDIT_RUNS_CSV}."
        )
        with open(AUDIT_RUNS_CSV, "r", encoding="utf-8") as f:
            content = f.read()
        assert content == TRUTH_AUDIT_RUNS_CSV, (
            f"{AUDIT_RUNS_CSV} content is not as expected.\n"
            "If you modified the input file, please revert it exactly to the original state."
        )

    def test_audit_runs_jsonl_exists_and_correct(self):
        """Check that /home/user/audit_runs.jsonl exists and matches the expected JSON Lines output."""
        assert os.path.isfile(AUDIT_RUNS_JSONL), (
            f"Missing required output file: {AUDIT_RUNS_JSONL}.\n"
            "You must generate this file as specified."
        )
        with open(AUDIT_RUNS_JSONL, "r", encoding="utf-8") as f:
            lines = [line.rstrip('\n') for line in f]
        assert len(lines) == len(TRUTH_AUDIT_RUNS_JSONL), (
            f"{AUDIT_RUNS_JSONL} should have {len(TRUTH_AUDIT_RUNS_JSONL)} lines, found {len(lines)}."
        )
        for idx, (line, truth_obj) in enumerate(zip(lines, TRUTH_AUDIT_RUNS_JSONL)):
            try:
                parsed = json.loads(line)
            except Exception as e:
                pytest.fail(
                    f"Line {idx+1} of {AUDIT_RUNS_JSONL} is not valid JSON: {e}\nLine: {line}"
                )
            # Check keys and types
            assert set(parsed.keys()) == set(truth_obj.keys()), (
                f"Line {idx+1} of {AUDIT_RUNS_JSONL} has incorrect fields.\n"
                f"Expected keys: {list(truth_obj.keys())}\nGot: {list(parsed.keys())}"
            )
            for k in truth_obj:
                assert parsed[k] == truth_obj[k], (
                    f"Line {idx+1} of {AUDIT_RUNS_JSONL}, field '{k}' mismatch.\n"
                    f"Expected: {truth_obj[k]!r}\nGot: {parsed[k]!r}"
                )
                assert isinstance(parsed[k], type(truth_obj[k])), (
                    f"Line {idx+1} of {AUDIT_RUNS_JSONL}, field '{k}' has wrong type.\n"
                    f"Expected type: {type(truth_obj[k])}, got: {type(parsed[k])}"
                )

    def test_audit_summary_csv_exists_and_correct(self):
        """Check that /home/user/audit_summary.csv exists and matches the expected summary CSV."""
        assert os.path.isfile(AUDIT_SUMMARY_CSV), (
            f"Missing required summary file: {AUDIT_SUMMARY_CSV}.\n"
            "You must generate this file as specified."
        )
        with open(AUDIT_SUMMARY_CSV, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            rows = [row for row in reader]
        # Check header and row count
        assert rows == TRUTH_AUDIT_SUMMARY_CSV, (
            f"{AUDIT_SUMMARY_CSV} content mismatch.\n"
            f"Expected:\n"
            + "\n".join([",".join(row) for row in TRUTH_AUDIT_SUMMARY_CSV])
            + "\nGot:\n"
            + "\n".join([",".join(row) for row in rows])
            + "\nCheck for extra spaces, wrong order, or wrong values."
        )

    def test_audit_task_log_exists_and_correct(self):
        """Check that /home/user/audit_task.log exists and contains the correct log lines."""
        assert os.path.isfile(AUDIT_TASK_LOG), (
            f"Missing required log file: {AUDIT_TASK_LOG}.\n"
            "You must generate this file as specified."
        )
        with open(AUDIT_TASK_LOG, "r", encoding="utf-8") as f:
            lines = f.readlines()
        assert lines == TRUTH_AUDIT_TASK_LOG, (
            f"{AUDIT_TASK_LOG} contents mismatch.\n"
            f"Expected:\n{''.join(TRUTH_AUDIT_TASK_LOG)}"
            f"Got:\n{''.join(lines)}"
            "Check for missing/extra lines, incorrect order, or missing newlines."
        )