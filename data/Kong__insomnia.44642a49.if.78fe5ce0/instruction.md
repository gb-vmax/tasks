# Bug Report

### Describe the bug

I'm experiencing an issue with HAR export when dealing with multipart/form-data requests that contain both file and text parameters. The exported HAR format appears to be mixing up which fields should be included for file vs non-file parameters.

### Reproduction

When exporting a request with form data parameters to HAR format:

```js
const body = {
  mimeType: 'multipart/form-data',
  params: [
    { name: 'textField', value: 'some text', type: 'text' },
    { name: 'fileField', fileName: 'document.pdf', type: 'file' }
  ]
};
```

The resulting HAR output has the wrong fields for each parameter type:
- Text parameters are getting `fileName` instead of `value`
- File parameters are getting `value` instead of `fileName`

### Expected behavior

According to the HAR spec:
- Text/non-file parameters should have `name` and `value` fields
- File parameters should have `name` and `fileName` fields

The export should correctly distinguish between these two types and include the appropriate fields for each.

### System Info
- Insomnia version: latest
- OS: macOS

This is causing issues when trying to import the exported HAR files into other tools, as they expect the correct field structure for form data parameters.

---
Repository: /testbed
