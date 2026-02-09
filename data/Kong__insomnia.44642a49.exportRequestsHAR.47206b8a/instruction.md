# Bug Report

### Describe the bug
When exporting requests to HAR format, the export is not including all the expected requests. It seems like requests are being skipped even when they should be included in the export.

### Reproduction
```js
// Create a workspace with some requests
const workspace = await createWorkspace();
const request1 = await createRequest(workspace);
const request2 = await createRequest(workspace);

// Try to export requests to HAR
const harExport = await exportRequestsHAR([request1, request2]);

// Expected: Both requests in the export
// Actual: Some or all requests are missing from the export
```

### Expected behavior
All requests that belong to valid workspaces should be included in the HAR export. The function should properly filter requests based on workspace availability and environment privacy settings.

### Additional context
This appears to affect the workspace lookup logic during the export process. When exporting multiple requests from the same workspace, some requests are being excluded unexpectedly.

---
Repository: /testbed
