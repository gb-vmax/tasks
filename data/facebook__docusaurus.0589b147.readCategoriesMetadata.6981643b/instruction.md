# Bug Report

### Describe the bug

When multiple category metadata files exist in the same folder, the sidebar configuration is not being read correctly. The system is picking the wrong file when there are duplicates, which causes the category metadata to be ignored or incorrectly applied.

### Reproduction

1. Create a folder with multiple category metadata files (e.g., `_category_.json` and `_category_.yml`)
2. Configure your sidebar to use categories
3. The second file's metadata is used instead of the first one

Expected: The first category metadata file should be used (with a warning about duplicates)
Actual: The second file is being selected, or in some cases an empty object is returned

### Additional context

This seems to be affecting how categories are displayed in the sidebar navigation. When I have multiple category files in a directory, the behavior is unpredictable - sometimes it picks the wrong file, and sometimes the category metadata seems to disappear entirely even when the file is valid.

The warning message about multiple files is shown, but the actual file being processed doesn't match what I'd expect based on the warning.

---
Repository: /testbed
