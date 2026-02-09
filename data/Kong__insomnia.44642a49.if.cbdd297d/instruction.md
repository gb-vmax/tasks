# Bug Report

### Describe the bug

I'm experiencing an issue with HAR export where file upload parameters and regular text parameters are being exported with incorrect fields. When I export a request that contains both file uploads and regular form data, the file parameters are getting `value` fields instead of `fileName`, and text parameters are getting `fileName` fields instead of `value`.

### Reproduction

```js
// Create a request with multipart form data containing:
// 1. A regular text parameter
// 2. A file upload parameter

const request = {
  body: {
    mimeType: 'multipart/form-data',
    params: [
      { name: 'username', value: 'john', type: 'text' },
      { name: 'avatar', fileName: 'photo.jpg', type: 'file' }
    ]
  }
};

// Export to HAR format
const harData = exportToHAR(request);

// The exported HAR has the fields swapped:
// - Text parameter has fileName instead of value
// - File parameter has value instead of fileName
```

### Expected behavior

The HAR export should correctly map:
- File type parameters → `fileName` field
- Text type parameters → `value` field

Currently it's doing the opposite, which breaks HAR imports in other tools.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
