# Bug Report

### Describe the bug

When exporting HAR files with file-based request bodies, the generated HAR output is missing critical information. The `mimeType` field is not being set for file uploads, and the body structure appears to be incomplete or malformed.

### Reproduction

```js
const renderedRequest = {
  body: {
    fileName: '/path/to/document.pdf',
    mimeType: 'application/pdf'
  }
}

// Export to HAR format
const harData = getRequestPostData(renderedRequest);

// Expected: harData should include mimeType and properly formatted text
// Actual: mimeType is missing or not properly detected
```

### Expected behavior

When a request includes a file body, the HAR export should:
1. Include the correct `mimeType` field in the postData
2. Read the file content and encode it as base64 in the `text` field
3. Handle both explicit mimeType from the request and auto-detection from file extension

Currently it seems like the mimeType is being lost during the export process, which breaks HAR import in other tools.

### System Info
- Insomnia version: latest
- OS: macOS

This is affecting our ability to export and share request collections with file uploads. Any help would be appreciated!

---
Repository: /testbed
