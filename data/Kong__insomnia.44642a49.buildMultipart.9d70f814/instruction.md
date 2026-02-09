# Bug Report

### Describe the bug

I'm experiencing an issue with multipart form data requests where the Content-Length header appears to be incorrect. When sending requests with file uploads, the server is rejecting them or they're getting truncated.

### Reproduction

```js
// Create a multipart request with file parameters
const params = [
  {
    type: 'file',
    name: 'upload',
    fileName: 'test.txt'
  }
];

// Build and send the multipart request
const multipart = await buildMultipart(params);
// The contentLength in the result doesn't match the actual body size
```

When I inspect the raw request being sent, the Content-Length header doesn't match the actual size of the multipart body. This causes issues with servers that validate content length or when uploading larger files.

### Expected behavior

The Content-Length header should accurately reflect the total size of the multipart request body, including all boundaries, headers, line breaks, and file content.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
