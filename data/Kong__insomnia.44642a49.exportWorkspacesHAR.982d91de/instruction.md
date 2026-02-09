# Bug Report

### Describe the bug
When exporting workspaces to HAR format, the export appears to be empty or missing all the actual requests. The exported HAR file doesn't contain any of the HTTP requests that should be included from the workspace.

### Reproduction
```js
// Export multiple workspaces to HAR
const workspaces = [workspace1, workspace2];
const harExport = await exportWorkspacesHAR(workspaces, false);

// Result: HAR file is generated but contains no requests
// Expected: HAR file should contain all requests from the workspaces
```

Steps to reproduce:
1. Create a workspace with several HTTP requests
2. Call `exportWorkspacesHAR()` with the workspace
3. Check the exported HAR file
4. Notice that no requests are included in the export

### Expected behavior
The exported HAR file should contain all the requests from the specified workspaces. Currently it seems like the requests are being filtered out instead of being included.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
