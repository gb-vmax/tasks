# Bug Report

### Describe the bug

When multiple category metadata files exist in the same directory, the wrong file is being read. The system appears to be using an incorrect file path when loading category metadata, which can lead to unexpected behavior or errors.

### Reproduction

Create a scenario where multiple category metadata files exist in the same folder:

```
docs/
  folder/
    _category_.json
    _category_.yml
```

When the plugin tries to read the category metadata, it may select the wrong file or fail to read it correctly due to an incorrect path being used.

### Expected behavior

The plugin should:
1. Read the correct category metadata file (preferably the last one in the list)
2. Use the proper file path when reading the file content
3. Show a warning about multiple files but still work correctly

### System Info
- Docusaurus version: Latest
- Node version: 18.x

The warning message about multiple category metadata files is shown, but the actual file being read doesn't match what's expected, potentially causing issues with category configuration.

---
Repository: /testbed
