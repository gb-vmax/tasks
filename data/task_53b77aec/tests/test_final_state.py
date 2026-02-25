# test_final_state.py

import os
import pytest

K8S_PODS_JSON_PATH = "/home/user/k8s_pods.json"
RUNNING_PODS_CSV_PATH = "/home/user/running_pods.csv"

EXPECTED_CSV = (
    "pod_name\n"
    "nginx-7fdc69b969-abcde\n"
    "db-0\n"
    "nginx-7fdc69b969-fghij\n"
)

@pytest.mark.describe("Final OS state validation after student action")
class TestFinalState:

    def test_running_pods_csv_exists(self):
        assert os.path.isfile(RUNNING_PODS_CSV_PATH), (
            f"Missing required output file: {RUNNING_PODS_CSV_PATH}. "
            f"Ensure you have created the CSV file at the required path."
        )

    def test_running_pods_csv_content_exact(self):
        """
        Validates that /home/user/running_pods.csv contains exactly the expected content:
        - Header 'pod_name'
        - Only pod names with status 'Running' from the input JSON
        - Order preserved from input JSON
        - Each row is LF-terminated, including header and last line (total 4 lines)
        - No extra whitespace, no extra lines or columns
        """
        try:
            with open(RUNNING_PODS_CSV_PATH, "rb") as f:
                content_bytes = f.read()
        except Exception as e:
            pytest.fail(f"Could not read {RUNNING_PODS_CSV_PATH}: {e}")

        # We check for exact bytes, including LF endings only.
        expected_bytes = (
            b"pod_name\n"
            b"nginx-7fdc69b969-abcde\n"
            b"db-0\n"
            b"nginx-7fdc69b969-fghij\n"
        )

        if content_bytes != expected_bytes:
            # Show the diff in a readable way
            actual_lines = content_bytes.decode('utf-8', errors='replace').splitlines(keepends=True)
            expected_lines = expected_bytes.decode('utf-8').splitlines(keepends=True)
            msg = [
                f"CSV content mismatch in {RUNNING_PODS_CSV_PATH}.",
                "Expected EXACT content (including line endings):"
            ]
            msg += [f"    {repr(line)}" for line in expected_lines]
            msg.append("Actual content:")
            msg += [f"    {repr(line)}" for line in actual_lines]
            msg.append(
                "Check for:\n"
                "- Only pods with status 'Running' are present\n"
                "- Header is present and correct\n"
                "- Line endings are exactly LF '\\n' (not CRLF or missing)\n"
                "- No extra whitespace, no extra columns\n"
                "- File ends with a single LF after the last pod name"
            )
            pytest.fail('\n'.join(msg))

    def test_running_pods_csv_no_extra_rows(self):
        """
        Ensures there are exactly 4 lines: header + 3 pod names, each LF-terminated,
        and no extra blank lines or trailing whitespace.
        """
        with open(RUNNING_PODS_CSV_PATH, "r", encoding="utf-8", newline='') as f:
            lines = f.readlines()

        assert len(lines) == 4, (
            f"{RUNNING_PODS_CSV_PATH} should have exactly 4 lines (header + 3 pod names), "
            f"but found {len(lines)} lines. Actual lines:\n{lines}\n"
            "Check for extra blank lines or missing rows."
        )

        for i, line in enumerate(lines):
            assert line.endswith('\n'), (
                f"Line {i+1} in {RUNNING_PODS_CSV_PATH} does not end with LF '\\n'. "
                f"All lines must end with LF only. Line content: {repr(line)}"
            )

        # Check for no trailing whitespace or extra columns
        for i, line in enumerate(lines):
            if i == 0:
                expected = "pod_name\n"
                assert line == expected, (
                    f"Header row in {RUNNING_PODS_CSV_PATH} is incorrect. "
                    f"Expected: {repr(expected)}, Found: {repr(line)}"
                )
            else:
                # Should be just pod name + LF, no commas, no whitespace
                pod_name = line.rstrip('\n')
                assert pod_name in [
                    "nginx-7fdc69b969-abcde",
                    "db-0",
                    "nginx-7fdc69b969-fghij"
                ], (
                    f"Unexpected pod name in row {i+1}: {repr(pod_name)}. "
                    "Only pod names with status 'Running' should appear."
                )
                assert ',' not in pod_name, (
                    f"Row {i+1} in {RUNNING_PODS_CSV_PATH} contains a comma. "
                    "Only one column (pod_name) is allowed."
                )
                assert pod_name.strip() == pod_name, (
                    f"Row {i+1} in {RUNNING_PODS_CSV_PATH} has leading or trailing whitespace: {repr(line)}"
                )