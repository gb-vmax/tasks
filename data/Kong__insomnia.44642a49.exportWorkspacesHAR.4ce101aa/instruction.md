# Bug Report

### Describe the bug

When exporting workspaces to HAR format with `includePrivateDocs` set to `true`, private documents are being excluded from the export instead of included. The behavior is inverted - setting the flag to `true` acts like `false` and vice versa.

### Reproduction

```js
// Try to export workspaces WITH private docs
await exportWorkspacesHAR(workspaces, true);
// Result: Private docs are NOT included (but should be)

// Try to export workspaces WITHOUT private docs  
await exportWorkspacesHAR(workspaces, false);
// Result: Private docs ARE included (but shouldn't be)
```

### Expected behavior

When `includePrivateDocs` is set to `true`, the exported HAR file should contain private documents. When set to `false`, private documents should be excluded from the export.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
