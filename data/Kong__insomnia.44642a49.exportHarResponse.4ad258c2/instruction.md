# Bug Report

### Describe the bug

When exporting HAR files, responses are not being included correctly. Instead of getting the actual response data, I'm receiving empty/default response objects with status 0 and no headers or content.

### Reproduction

```js
// Export a request with a valid response
const response = {
  statusCode: 200,
  statusMessage: 'OK',
  headers: [...],
  // ... other response data
};

const harData = await exportHarResponse(response);

// Expected: HAR response with status 200 and actual data
// Actual: Empty response object with status 0
console.log(harData.status); // prints 0 instead of 200
```

### Expected behavior

The exported HAR response should contain the actual response data including status code, status message, headers, and content when a valid response object is provided.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have broken recently as HAR exports were working fine before. The response data exists but it's not being exported to the HAR format correctly.

---
Repository: /testbed
