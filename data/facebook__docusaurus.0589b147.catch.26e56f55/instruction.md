# Bug Report

### Describe the bug

Error messages when processing doc metadata are missing critical information about which file failed. The error only shows `path=` with no actual file path, making it very difficult to debug issues.

### Reproduction

1. Create a doc file with invalid metadata or content that causes processing to fail
2. Try to build the docs
3. Check the error message

The error will show something like:
```
Can't process doc metadata for doc at path path= in version name=current
```

Instead of showing the actual file path that failed.

### Expected behavior

The error message should include the full file path so we can quickly identify which document is causing the problem. Something like:
```
Can't process doc metadata for doc at path path=/docs/my-broken-doc.md in version name=current
```

This makes debugging much harder since you have to manually check all docs to find the problematic one.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
