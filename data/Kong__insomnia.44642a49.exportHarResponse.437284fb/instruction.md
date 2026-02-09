# Bug Report

### Describe the bug

After a recent update, HAR export is failing when trying to export responses with redirect status codes. The exported HAR file is missing the redirect URL information that should be extracted from the Location header.

### Reproduction

```js
// Export a response with a 301/302 redirect
const response = {
  statusCode: 302,
  statusMessage: 'Found',
  headers: [
    { name: 'Location', value: 'https://example.com/redirected' },
    { name: 'Content-Length', value: '0' }
  ]
};

const harResponse = await exportHarResponse(response);

// Expected: harResponse.redirectURL should be 'https://example.com/redirected'
// Actual: redirectURL is empty string even though Location header exists
```

### Expected behavior

When exporting a response with redirect status codes (3xx), the `redirectURL` field in the HAR output should contain the value from the `Location` header. Currently it's always returning an empty string regardless of whether a Location header is present.

### Additional context

This is breaking our HAR export functionality for any requests that involve redirects. The HAR specification requires the redirectURL field to be populated for redirect responses.

---
Repository: /testbed
