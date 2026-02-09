# Bug Report

### Describe the bug

When uploading files using multipart form data, the total size calculation is incorrect when a file doesn't exist or can't be accessed. The size is being added to `totalSize` even after an error occurs during `fs.statSync()`, and the file stream is still being created and piped despite the error.

### Reproduction

```js
// Try to send a multipart request with a file that doesn't exist
const params = [
  {
    type: 'file',
    name: 'upload',
    fileName: '/path/to/nonexistent/file.txt'
  }
];

await buildMultipart(params);
```

### Expected behavior

When a file cannot be accessed (e.g., file doesn't exist, permission denied), the function should:
1. Not add the file size to `totalSize` 
2. Not attempt to create a read stream for the file
3. Properly reject the promise without trying to process the file further

### Current behavior

The code attempts to add an undefined size to `totalSize` after catching an error, and still tries to create a file stream even though the file stat failed. This leads to multiple issues and potential crashes.

### System Info
- Insomnia version: latest
- OS: All platforms affected

---
Repository: /testbed
