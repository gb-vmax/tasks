# Bug Report

### Describe the bug

When multiple category metadata files exist in the same directory (e.g., `_category_.json`, `_category_.yml`, `_category_.yaml`), the wrong file is being selected. The system appears to be grouping files incorrectly and not picking the expected file when duplicates are present.

### Reproduction

Create a docs structure with multiple category metadata files:

```
docs/
  guides/
    _category_.json
    _category_.yml
```

When the sidebar is built, the wrong category metadata file gets used instead of the first one found. This causes unexpected category configurations to be applied.

### Expected behavior

When multiple category metadata files exist in the same folder, the first file found should be used consistently (with a warning about duplicates). The grouping logic should organize files by their directory path, not by their filename.

### System Info
- Docusaurus plugin: @docusaurus/plugin-content-docs

---
Repository: /testbed
