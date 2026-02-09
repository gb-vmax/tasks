# Bug Report

### Describe the bug

When exporting requests with file parameters to HAR format, the file and text parameters are getting mixed up. File parameters are being exported with `value` fields instead of `fileName`, and text parameters are getting `fileName` instead of `value`. This makes the exported HAR files invalid and unusable.

### Reproduction

```js
const request = {
  body: {
    mimeType: 'multipart/form-data',
    params: [
      { name: 'textField', value: 'some text', type: 'text' },
      { name: 'fileField', fileName: 'upload.pdf', type: 'file' }
    ]
  }
}

// Export to HAR
const harData = getRequestPostData(request);

// Expected: textField should have 'value', fileField should have 'fileName'
// Actual: textField has 'fileName', fileField has 'value'
```

### Expected behavior

- Text/form parameters should be exported with a `value` field
- File parameters should be exported with a `fileName` field
- The HAR format specification requires this distinction

### System Info
- Insomnia version: latest
- OS: macOS

This is breaking HAR exports for any requests that include file uploads.

---
Repository: /testbed
