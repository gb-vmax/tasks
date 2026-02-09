# Bug Report

### Describe the bug

When exporting HAR files, the `redirectURL` field is always empty even when the response is a redirect (3xx status code). According to the HAR specification, this field should contain the redirect target URL from the `Location` header when the response status is in the 3xx range.

### Reproduction

```js
// Export a response with a redirect status
const response = {
  statusCode: 302,
  statusMessage: 'Found',
  headers: [
    { name: 'Location', value: 'https://example.com/redirected' },
    { name: 'Content-Type', value: 'text/html' }
  ]
}

const harResponse = await exportHarResponse(response);

// Expected: harResponse.redirectURL = 'https://example.com/redirected'
// Actual: harResponse.redirectURL = ''
```

### Expected behavior

When a response has a 3xx status code and contains a `Location` header, the `redirectURL` field in the exported HAR should be populated with the value from that header. Currently it's always set to an empty string.

Also noticed that `headersSize` and `bodySize` are always set to `-1` instead of calculating the actual sizes, which makes the HAR file less useful for performance analysis.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
