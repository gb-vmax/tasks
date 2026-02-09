# Bug Report

### Describe the bug

When exporting multiple workspaces, only the first workspace's data is being exported repeatedly instead of exporting each workspace individually. Additionally, the export appears to be filtering out all requests instead of including them, resulting in empty or nearly empty exports.

### Reproduction

```js
// Setup multiple workspaces with different requests
const workspace1 = { id: 'ws1', name: 'Workspace 1' };
const workspace2 = { id: 'ws2', name: 'Workspace 2' };

// Each workspace has different requests (HTTP, gRPC, WebSocket)
// Try to export both workspaces
await exportWorkspacesData(
  [workspace1, workspace2],
  true,
  'json'
);

// Result: Only workspace1's data is exported twice
// Expected: Both workspace1 and workspace2 data should be exported
```

### Expected behavior

- Each workspace in the array should be processed individually
- All request types (HTTP requests, gRPC requests, and WebSocket requests) should be included in the export
- The exported data should contain requests from all provided workspaces

### Actual behavior

- Only the first workspace's data is being exported for all workspaces in the array
- No requests are being included in the export (appears to be filtering out everything)

This is affecting our ability to backup and migrate multiple workspaces at once. Any workspace export beyond the first one is just a duplicate of the first workspace's data.

---
Repository: /testbed
