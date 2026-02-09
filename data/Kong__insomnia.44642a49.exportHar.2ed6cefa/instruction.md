# Bug Report

### Describe the bug

When exporting multiple requests to HAR format, the last request in the list is being excluded from the export. Only the first N-1 requests are included in the generated HAR file.

### Reproduction

```js
const exportRequests = [
  { requestId: 'req1', environmentId: 'env1' },
  { requestId: 'req2', environmentId: 'env1' },
  { requestId: 'req3', environmentId: 'env1' }
];

const har = await exportHar(exportRequests);

// Expected: 3 entries in HAR
// Actual: Only 2 entries (req1 and req2), req3 is missing
console.log(har.log.entries.length); // outputs 2 instead of 3
```

### Expected behavior

All requests passed to `exportHar()` should be included in the exported HAR file. If I provide 3 requests, the HAR should contain 3 entries.

### Additional context

This seems to affect any export with multiple requests - the last one is always dropped. Single request exports work fine.

---
Repository: /testbed
