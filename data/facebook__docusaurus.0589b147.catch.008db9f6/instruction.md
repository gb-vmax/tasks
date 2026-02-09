# Bug Report

### Describe the bug

When processing doc metadata fails, the error message shows `undefined` for the file path instead of the actual file path. This makes it really difficult to debug which document is causing the issue.

### Reproduction

1. Create a docs file that will trigger a metadata processing error (e.g., invalid frontmatter)
2. Build the site
3. Observe the error message - it will show `path=undefined` instead of the actual file path

The error message looks like:
```
Can't process doc metadata for doc at path path=undefined in version name=...
```

### Expected behavior

The error message should display the actual file path to help identify which document is causing the problem, like:
```
Can't process doc metadata for doc at path path=docs/my-doc.md in version name=...
```

This makes it much harder to track down problematic docs in a large documentation site.

---
Repository: /testbed
