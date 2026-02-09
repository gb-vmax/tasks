# Bug Report

### Describe the bug

When exporting multiple workspaces to HAR format, only one workspace is being exported instead of all selected workspaces. It seems like the export function is not properly collecting documents from all workspaces.

### Reproduction

```js
// Select multiple workspaces for export
const workspaces = [workspace1, workspace2, workspace3];

// Try to export all workspaces to HAR
await exportWorkspacesHAR(workspaces, includePrivateDocs);

// Result: Only gets requests from one workspace instead of all three
```

### Steps to reproduce:
1. Create multiple workspaces with requests
2. Select all workspaces for HAR export
3. Perform the export operation
4. Check the exported HAR file

### Expected behavior

All requests from all selected workspaces should be included in the exported HAR file. If I select 3 workspaces with 5 requests each, I should get 15 requests in the export, not just 5.

### Actual behavior

Only requests from a single workspace are being exported, even when multiple workspaces are selected.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
