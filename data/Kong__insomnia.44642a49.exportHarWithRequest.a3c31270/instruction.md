# Bug Report

### Describe the bug
When exporting HAR files with requests, the `addContentLength` parameter behavior appears to be inverted. If I pass `true` to include the Content-Length header, it gets excluded, and vice versa.

### Reproduction
```js
// Try to export HAR with Content-Length header
const har = await exportHarWithRequest(request, true);

// Expected: Content-Length header should be present
// Actual: Content-Length header is missing

// Try to export HAR without Content-Length header
const har2 = await exportHarWithRequest(request, false);

// Expected: Content-Length header should be absent
// Actual: Content-Length header is present
```

### Expected behavior
When `addContentLength` is set to `true`, the exported HAR should include the Content-Length header. When set to `false`, it should be excluded.

### Additional context
This seems to affect all HAR exports. The parameter is being passed with the opposite boolean value than what's intended.

---
Repository: /testbed
