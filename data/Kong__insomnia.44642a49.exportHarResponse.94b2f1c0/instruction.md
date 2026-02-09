# Bug Report

### Describe the bug

The HAR export is now calculating `headersSize` and `bodySize` values, but the calculation appears to be incorrect. The `headersSize` is being computed by assuming HTTP/1.1 protocol and manually constructing the status line and headers, but this doesn't account for the actual protocol used in the response. Additionally, the calculation adds 2 bytes for the final CRLF, which may not accurately reflect the actual headers size transmitted.

### Reproduction

```js
// Export a response with custom headers
const response = {
  statusCode: 200,
  statusMessage: 'OK',
  headers: [
    { name: 'Content-Type', value: 'application/json' },
    { name: 'Content-Length', value: '123' }
  ],
  // ... other response data
};

const harResponse = await exportHarResponse(response);
console.log(harResponse.headersSize); // Shows calculated size
// Expected: Should match actual transmitted header size
```

The `headersSize` calculation hardcodes "HTTP/1.1" in the status line regardless of the actual HTTP version used. For HTTP/2 or HTTP/3 responses, this will produce an incorrect size since these protocols don't transmit headers in the same text format.

Also, when extracting redirect URLs, the code only checks for status codes in the 3xx range, but doesn't handle cases where the Location header might be present with other status codes (like 201 Created).

### Expected behavior

The `headersSize` should accurately reflect the size of headers as they were actually transmitted, taking into account the HTTP protocol version. For HTTP/2 and HTTP/3, header sizes are calculated differently due to HPACK/QPACK compression.

The `redirectURL` should be extracted based on the presence of a Location header, not just the status code range.

### System Info
- Insomnia version: latest
- Platform: Cross-platform issue

---
Repository: /testbed
