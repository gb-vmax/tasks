# Bug Report

### Describe the bug

I'm experiencing issues with multipart form data requests - the content length appears to be incorrect and the requests are failing. The multipart boundary delimiter also seems malformed in the generated output.

### Reproduction

When sending a multipart/form-data request with file uploads or form fields, the request fails or behaves unexpectedly. 

Steps to reproduce:
1. Create a multipart request with one or more parameters
2. Add some text fields and/or file uploads
3. Send the request
4. The server rejects it or the content length doesn't match the actual payload size

Example request setup:
```js
const params = [
  { name: 'field1', value: 'test data' },
  { name: 'file', fileName: 'test.txt', type: 'text/plain' }
];
```

### Expected behavior

The multipart request should be properly formatted with:
- Correct content-length header matching the actual payload size
- Proper boundary delimiters (should end with `--boundary--`)
- All form fields and files included correctly

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have started recently - multipart requests were working fine before. The content-length calculation seems off by a few bytes and the boundary terminator looks incorrect.

---
Repository: /testbed
