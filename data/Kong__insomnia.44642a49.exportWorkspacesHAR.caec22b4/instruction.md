# Bug Report

### Describe the bug

When exporting workspaces to HAR format with `includePrivateDocs` set to `true`, private documents are not being included in the export. Instead, they're being filtered out as if the parameter was set to `false`.

### Reproduction

```js
// Try exporting workspaces with private docs included
await exportWorkspacesHAR(myWorkspaces, true);

// Expected: Private documents should be included in the HAR export
// Actual: Private documents are excluded from the export
```

Steps to reproduce:
1. Create a workspace with some private documents/requests
2. Call `exportWorkspacesHAR()` with `includePrivateDocs` set to `true`
3. Check the exported HAR file
4. Notice that private documents are missing

### Expected behavior

When `includePrivateDocs` is set to `true`, all documents including private ones should be included in the HAR export. When set to `false`, private documents should be excluded.

Currently it seems like the behavior is inverted - setting it to `true` excludes private docs and setting it to `false` includes them.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
