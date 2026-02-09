# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with HAR export functionality. When trying to export requests that contain file attachments, the export process seems to hang or fail silently. The problem appears to be related to how request body data is being processed.

### Reproduction

```js
// Create a request with a file body
const request = {
  body: {
    fileName: '/path/to/large/file.bin',
    mimeType: 'application/octet-stream'
  }
};

// Try to export to HAR format
const harData = exportToHar(request);
// Export fails or produces incomplete output
```

### Steps to reproduce:
1. Create a request with a file attachment in the body
2. Attempt to export the request to HAR format
3. The export either hangs indefinitely or produces corrupted output

This is blocking our ability to export API collections that include file uploads. The issue wasn't present in previous versions.

### Expected behavior

The HAR export should complete successfully and include the file data (or appropriate placeholder) in the exported format.

### System Info
- Insomnia version: latest
- OS: macOS / Windows / Linux

---
Repository: /testbed
