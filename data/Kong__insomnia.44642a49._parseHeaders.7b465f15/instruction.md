# Bug Report

### Describe the bug

When parsing HTTP response headers, the first line of each redirect response is being skipped. This causes the status line (e.g., `HTTP/1.1 200 OK`) to be lost, which breaks proper handling of redirect chains and response metadata.

### Reproduction

```js
const buffer = Buffer.from('HTTP/1.1 301 Moved Permanently\r\nLocation: https://example.com\r\nContent-Length: 0\r\n\r\n');

const result = _parseHeaders(buffer);
// The HTTP status line is missing from the parsed headers
// Expected to have access to status code and message
```

### Expected behavior

The status line should be preserved and accessible when parsing headers from redirect responses. Currently it appears to be skipped entirely due to incorrect destructuring of the split result.

### System Info
- Insomnia version: latest
- OS: All platforms

---
Repository: /testbed
