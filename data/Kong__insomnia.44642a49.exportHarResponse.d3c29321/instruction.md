# Bug Report

### Describe the bug

When exporting HAR files, the `headersSize` and `bodySize` fields are now being populated with calculated values instead of `-1`. However, the `headersSize` calculation appears to be incorrect - it's using a hardcoded `HTTP/1.1` version in the status line calculation, but the actual response might be using a different HTTP version (like HTTP/2 or HTTP/1.0).

Additionally, the redirect URL extraction logic assumes that all 3xx status codes should have a Location header, but this isn't always the case (e.g., 304 Not Modified responses don't redirect).

### Reproduction

```js
// Export a HAR file with a response that uses HTTP/2
const response = {
  statusCode: 200,
  statusMessage: 'OK',
  httpVersion: 'HTTP/2',
  headers: [
    { name: 'Content-Type', value: 'application/json' },
    { name: 'Content-Length', value: '100' }
  ]
};

const harResponse = await exportHarResponse(response);

// The headersSize will be calculated incorrectly because it assumes HTTP/1.1
console.log(harResponse.headersSize); // Incorrect size due to wrong HTTP version
```

Another case:
```js
// 304 Not Modified response without Location header
const response = {
  statusCode: 304,
  statusMessage: 'Not Modified',
  headers: []
};

const harResponse = await exportHarResponse(response);
console.log(harResponse.redirectURL); // Returns empty string, but the logic still tries to find Location header
```

### Expected behavior

The `headersSize` calculation should use the actual HTTP version from the response object, not a hardcoded `HTTP/1.1`. The redirect URL extraction should also be more robust and handle edge cases properly.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
