# Bug Report

### Describe the bug

When there are multiple category metadata files in the same folder, the wrong file is being read. The system is trying to read from the folder path instead of the actual file path, which causes file reading errors.

### Reproduction

1. Create a docs folder with multiple category metadata files in the same directory (e.g., `_category_.json` and `_category_.yml`)
2. Try to build the documentation
3. The build process fails or reads incorrect metadata because it's attempting to read from the directory path instead of the file path

### Expected behavior

When multiple category metadata files exist in the same folder, the system should:
1. Read from the correct file path (not the folder path)
2. Use the first file in the list consistently (or provide clear documentation on which file takes precedence)

The warning message indicates that the behavior is undetermined when multiple files exist, but the actual file reading should still work correctly.

### Additional context

This appears to be related to how the file path is constructed when reading category metadata. The path being used for `fs.readFile` seems incorrect.

---
Repository: /testbed
