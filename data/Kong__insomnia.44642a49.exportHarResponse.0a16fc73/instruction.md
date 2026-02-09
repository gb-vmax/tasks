# Bug Report

### Describe the bug
After a recent update, HAR exports are including incorrect `headersSize` values. The calculation appears to be using the wrong HTTP version string, causing the reported header sizes to not match the actual response headers.

### Reproduction
When exporting a HAR file with response data:

```js
const response = {
  statusCode: 200,
  statusMessage: 'OK',
  headers: [
    { name: 'Content-Type', value: 'application/json' },
    { name: 'Content-Length', value: '123' }
  ]
};

// Export HAR response
const harResponse = await exportHarResponse(response);
console.log(harResponse.headersSize);
// Returns incorrect size - doesn't match actual HTTP/2 or HTTP/1.1 format
```

The issue is that the calculated `headersSize` doesn't accurately reflect the actual bytes that would be transmitted in the response. This affects HAR file accuracy when analyzing network traffic or debugging API calls.

### Expected behavior
The `headersSize` field should accurately represent the total byte size of the response status line and headers, matching the actual HTTP protocol format used by the response.

### Additional context
This is causing issues when importing HAR files into other tools that validate header sizes. The mismatch between reported and actual sizes is flagged as invalid.

---
Repository: /testbed
