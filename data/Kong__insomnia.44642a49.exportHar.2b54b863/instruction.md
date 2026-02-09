# Bug Report

### Describe the bug
HAR export is broken after recent changes. When trying to export HAR files, the export process fails and doesn't generate a valid HAR file.

### Reproduction
```js
// Try to export HAR for any request
const exportRequests = [
  {
    request: myRequest,
    response: myResponse
  }
];

await exportHar(exportRequests);
// This fails to complete
```

### Expected behavior
The HAR export should complete successfully and generate a valid HAR file with all request/response data.

### Additional context
This seems to have started happening recently. The export function appears to be incomplete or cut off mid-implementation. The `startedDateTime` line looks malformed with `.t` at the end instead of a proper method call.

---
Repository: /testbed
