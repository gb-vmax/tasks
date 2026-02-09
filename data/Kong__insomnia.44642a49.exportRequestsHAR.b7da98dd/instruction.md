# Bug Report

### Describe the bug

When exporting requests to HAR format, requests are not being included in the export even when they should be. It appears that the workspace lookup logic is incorrectly filtering out valid workspaces, resulting in an incomplete HAR export.

### Reproduction

```js
// Set up a workspace with some requests
const workspace = { _id: 'workspace_1', name: 'My Workspace' };
const request = { _id: 'req_1', name: 'Test Request' };

// Try to export requests to HAR
await exportRequestsHAR(requests, includePrivateDocs);

// Expected: All requests from the workspace should be included
// Actual: Requests are missing from the HAR export
```

### Steps to reproduce:
1. Create a workspace with multiple requests
2. Attempt to export those requests to HAR format
3. Check the exported HAR file

### Expected behavior

All requests belonging to valid workspaces should be included in the HAR export. The workspace lookup should correctly identify when a workspace has already been processed.

### Additional context

This seems to affect the deduplication logic when processing multiple requests from the same workspace. The export may be skipping requests that should be included.

---
Repository: /testbed
