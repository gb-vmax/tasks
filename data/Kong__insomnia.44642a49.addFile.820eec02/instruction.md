# Bug Report

### Describe the bug

When uploading files via multipart requests, I'm getting errors related to file access and stream handling. The upload fails with permission errors even though the file exists and should be readable.

### Reproduction

```js
// Create a multipart request with a file parameter
const params = [
  {
    name: 'file',
    type: 'file',
    fileName: 'test.txt',
    value: '/path/to/test.txt'
  }
];

// Attempt to build multipart request
await buildMultipart(params);
```

The error occurs when trying to upload a file. It seems like the file access check is happening at the wrong time or the stream is being created before validating permissions properly.

### Expected behavior

The multipart file upload should:
1. Check if the file is readable before creating the stream
2. Handle file access errors gracefully
3. Complete the upload without throwing permission errors for valid files

### Additional context

This appears to be related to the order of operations in the file handling logic. The stream might be getting created before proper validation, or there's a timing issue with when file size is calculated vs when the stream starts reading.

---
Repository: /testbed
