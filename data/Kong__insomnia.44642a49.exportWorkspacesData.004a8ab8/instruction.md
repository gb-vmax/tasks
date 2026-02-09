# Bug Report

### Describe the bug

When exporting multiple workspaces, only one workspace's data is being exported instead of all selected workspaces. It seems like the export is completing too early and not waiting for all workspace data to be collected.

### Reproduction

```js
// Select multiple workspaces for export
const workspaces = [workspace1, workspace2, workspace3];

// Try to export all workspaces
await exportWorkspacesData(workspaces, includePrivateDocs, 'json');

// Result: Only exports data from the first workspace that completes
// Expected: Should export data from all 3 workspaces
```

Steps to reproduce:
1. Create multiple workspaces with different requests
2. Select all workspaces for export
3. Export to JSON or YAML format
4. Check the exported file - it only contains data from one workspace

### Expected behavior

The export should include all requests from all selected workspaces, not just the first one that finishes processing.

### Additional context

Also noticed that the exported file seems to be missing some request types. For example, if I have both REST requests and WebSocket requests in my workspace, only certain combinations are being included in the export.

---
Repository: /testbed
