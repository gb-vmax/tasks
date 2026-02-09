# Bug Report

### Describe the bug

When sending multipart form data requests, the request body appears to be malformed. The multipart boundary delimiter is being duplicated, which causes the server to reject or incorrectly parse the request.

### Reproduction

```js
const params = [
  {
    name: 'field1',
    value: 'test value',
    type: 'text'
  },
  {
    name: 'file',
    fileName: 'test.txt',
    type: 'file'
  }
];

const result = await buildMultipart(params);
// The resulting multipart body has an extra boundary line before the closing boundary
```

### Expected behavior

The multipart request should have a properly formatted body with a single closing boundary delimiter (`--boundary--`). Currently, there's an extra boundary line being added before the final closing delimiter, which breaks the multipart format specification.

According to RFC 2046, the multipart body should end with a single closing boundary marker, but the generated output includes an additional boundary line that shouldn't be there.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
