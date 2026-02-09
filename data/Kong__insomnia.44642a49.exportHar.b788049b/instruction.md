# Bug Report

### Describe the bug

When exporting HAR files with multiple requests, the first request in the list is being skipped and not included in the exported HAR file. This results in incomplete exports where only requests starting from the second one are present.

### Reproduction

```js
const exportRequests = [
  { requestId: 'req1', responseId: 'res1' },
  { requestId: 'req2', responseId: 'res2' },
  { requestId: 'req3', responseId: 'res3' }
];

const har = await exportHar(exportRequests);

// Expected: 3 entries in HAR
// Actual: Only 2 entries (req2 and req3), req1 is missing
console.log(har.log.entries.length); // Returns 2 instead of 3
```

### Steps to reproduce

1. Create a workspace with multiple requests
2. Export all requests to HAR format
3. Check the exported HAR file
4. Notice that the first request is missing from the export

### Expected behavior

All requests passed to `exportHar()` should be included in the exported HAR file, including the first one in the array.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
