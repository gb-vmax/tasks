# Bug Report

### Describe the bug

When exporting requests to HAR format, workspaces are not being properly included in the export. It seems like the export logic is inverted - workspaces that should be included are being skipped, and the environment filtering is also behaving incorrectly.

### Reproduction

```js
// Setup multiple workspaces with requests
const workspace1 = await createWorkspace({ name: 'Workspace 1' });
const workspace2 = await createWorkspace({ name: 'Workspace 2' });

// Add requests to both workspaces
const request1 = await createRequest({ workspaceId: workspace1._id });
const request2 = await createRequest({ workspaceId: workspace2._id });

// Try to export all requests
const harExport = await exportRequestsHAR([request1, request2]);

// Expected: Both workspaces should be in the export
// Actual: Only one workspace appears, or workspaces are duplicated
```

### Expected behavior

- Each workspace should only be processed once during export
- Workspaces associated with the selected requests should be included in the HAR export
- Private environments should be excluded unless `includePrivateDocs` is true
- All requests from included workspaces should appear in the final export

### Additional context

This appears to affect the HAR export functionality. When trying to export a collection of requests from different workspaces, the resulting HAR file either contains duplicate workspace entries or is missing some workspaces entirely. The environment filtering also seems backwards - private environments are being included when they shouldn't be, and vice versa.

---
Repository: /testbed
