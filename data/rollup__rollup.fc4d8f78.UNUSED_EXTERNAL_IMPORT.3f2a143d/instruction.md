# Bug Report

### Describe the bug

When I have multiple unused external imports from different files, the warning messages are showing incorrect file paths. All warnings are displaying the same file path instead of showing the actual file where each unused import is located.

### Reproduction

1. Create multiple files that import from the same external module but don't use those imports
2. Run the build
3. Check the "Unused external imports" warnings

For example, if I have:
- `file1.js` imports `foo` from `external-lib` (unused)
- `file2.js` imports `bar` from `external-lib` (unused)
- `file3.js` imports `baz` from `external-lib` (unused)

The warnings all show the path from the first file instead of showing `file1.js`, `file2.js`, and `file3.js` respectively.

### Expected behavior

Each warning should display the correct file path where the unused import actually occurs. The warning message should show which specific file has the unused import, not just reuse the first file's path for all warnings.

### Additional context

This seems to have broken recently. The warnings used to show the correct file paths for each unused import.

---
Repository: /testbed
