# Bug Report

### Describe the bug

When multiple category metadata files exist in the same folder, the sidebar is using the wrong file. It appears the first file is being selected instead of the last one, which causes incorrect category metadata to be loaded.

Additionally, when there's an error parsing the category metadata file, the error message shows the folder path instead of the actual file path that failed to parse. This makes it difficult to identify which specific file is causing the problem.

### Reproduction

1. Create a docs folder with multiple category metadata files (e.g., `_category_.yml` and `_category_.json`)
2. Configure different metadata in each file
3. Build the documentation
4. The wrong category metadata is applied (from the first file instead of the last)

Also, if you introduce a syntax error in one of the category metadata files:
1. The error message will show the folder path instead of the specific file path
2. This makes debugging much harder when you have multiple metadata files

### Expected behavior

- When multiple category metadata files exist, the last file should be used (as indicated by the warning message logic)
- Error messages should display the actual file path that failed to parse, not the folder path

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
