# Bug Report

### Describe the bug
When exporting requests to HAR format, the requests appear in the wrong order in the exported file. The sorting seems to be reversed from what it should be.

### Reproduction
```js
// Create multiple requests with different metaSortKey values
const requests = [
  { _id: '1', metaSortKey: 100 },
  { _id: '2', metaSortKey: 200 },
  { _id: '3', metaSortKey: 300 }
];

// Export to HAR
const harExport = await exportRequestsHAR(requests);

// The requests appear in reverse order (300, 200, 100)
// instead of the expected order (100, 200, 300)
```

### Expected behavior
Requests should be sorted in ascending order based on their `metaSortKey` property in the exported HAR file. Currently they appear to be sorted in descending order instead.

### Additional context
This affects the usability of exported HAR files since the request order doesn't match what's shown in the UI.

---
Repository: /testbed
