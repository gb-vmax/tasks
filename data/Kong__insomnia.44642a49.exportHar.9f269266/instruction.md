# Bug Report

### Describe the bug
When exporting HAR files with multiple requests, the response fetching logic seems to be inverted. If a specific `responseId` is provided, the code tries to get the latest response instead of using the provided ID. Conversely, when no `responseId` is provided, it attempts to fetch by ID (which would be undefined/null).

### Reproduction
```js
// When exporting with a specific responseId
const exportRequests = [{
  requestId: 'req_123',
  responseId: 'res_456',  // Specific response ID provided
  environmentId: 'env_789'
}];

await exportHar(exportRequests);

// The export uses getLatestForRequest instead of getById
// So it ignores the specific responseId that was passed in
```

### Expected behavior
- When `responseId` is provided, it should use `getById(responseId)` to fetch that specific response
- When `responseId` is NOT provided (null/undefined), it should use `getLatestForRequest()` to get the most recent response

Currently the logic appears to be backwards - it does the opposite of what's expected.

### System Info
- Version: Latest from main branch

---
Repository: /testbed
