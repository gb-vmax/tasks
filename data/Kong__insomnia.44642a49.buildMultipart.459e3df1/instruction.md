# Bug Report

### Describe the bug

When sending multipart form data requests with file uploads, the Content-Length header appears to be incorrect. The request seems to be missing part of the file data or the size calculation is off, causing issues with servers that strictly validate the Content-Length.

### Reproduction

```js
// Create a multipart request with a file upload
const params = [
  {
    name: 'file',
    type: 'file',
    fileName: 'test.txt',
    value: '/path/to/file.txt'
  },
  {
    name: 'description',
    type: 'text',
    value: 'Test file upload'
  }
]

// Build and send the multipart request
// The Content-Length header doesn't match the actual body size
```

### Expected behavior

The Content-Length header should accurately reflect the total size of the multipart body, including all file streams and text fields. Servers should be able to receive the complete request without errors.

### Additional context

This seems to affect requests with file attachments specifically. Text-only multipart requests might work fine, but when files are included, the size calculation appears to be incomplete. Some servers return 400 Bad Request or timeout waiting for more data.

---
Repository: /testbed
