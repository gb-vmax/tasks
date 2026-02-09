# Bug Report

### Describe the bug

When uploading files using multipart form data, the file content is not being fully written to the request body. The multipart request completes prematurely, resulting in incomplete or corrupted file uploads.

### Reproduction

```js
// Create a multipart request with a file attachment
const params = [
  {
    name: 'file',
    type: 'file',
    fileName: 'test.pdf',
    value: '/path/to/large/file.pdf'
  }
];

// Build and send the multipart request
const result = await buildMultipart(params);
// File upload completes too early, resulting in truncated/incomplete file
```

### Expected behavior

The file should be completely read and written to the multipart request body before the request is considered complete. All bytes of the file should be included in the upload.

### Additional context

This seems to affect larger files more noticeably. Small files might work by coincidence, but larger files consistently get truncated. The request finishes before the file stream has finished reading/writing all the data.

---
Repository: /testbed
