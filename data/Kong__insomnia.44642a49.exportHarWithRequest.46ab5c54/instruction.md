# Bug Report

### Describe the bug

After a recent update, HAR exports are getting cut off or incomplete. When exporting requests to HAR format, the export seems to terminate prematurely and doesn't return the full HAR request object.

### Reproduction

```js
const request = {
  _id: 'req_123',
  modified: Date.now(),
  // ... other request properties
};

const harExport = await exportHarWithRequest(request, 'env_id', true);
// harExport is incomplete or malformed
```

### Expected behavior

The `exportHarWithRequest` function should return a complete and valid HAR request object. The export should include all request data and any plugin modifications that were applied.

### Additional context

This appears to happen consistently when exporting requests with the `addContentLength` parameter set to true. The export starts but seems to get truncated before completion. Not sure if this is related to the caching logic or something else.

---
Repository: /testbed
