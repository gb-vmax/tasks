# Bug Report

### Describe the bug

When exporting requests with form data parameters to HAR format, the parameter types are being incorrectly mapped. File parameters are being exported with `value` fields instead of `fileName`, and text parameters are getting `fileName` instead of `value`.

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

// Export to HAR format
const harData = exportToHar(request)

// The output has swapped fields:
// textField gets fileName instead of value
// fileField gets value instead of fileName
```

### Expected behavior

- Text/form parameters should export with a `value` field containing the parameter value
- File parameters should export with a `fileName` field containing the file name
- The HAR export should also include the `mimeType` field

### System Info
- Insomnia version: latest
- OS: macOS

This is causing issues when trying to import the exported HAR files into other tools, as the parameter types don't match the HAR specification.

---
Repository: /testbed
