# Bug Report

### Describe the bug

The `contentInfo()` method appears to be broken or incomplete. When trying to access response content information, the method doesn't return the expected data structure and may be causing runtime errors.

### Reproduction

```js
const response = new Response({
  headers: [
    { key: 'Content-Type', value: 'application/json; charset=utf-8' },
    { key: 'Content-Disposition', value: 'attachment; filename="data.json"' }
  ],
  body: '{"test": "data"}'
});

// This should return mime type, format, charset, and file info
const info = response.contentInfo();
console.log(info);
// Expected: { mimeType, mimeFormat, charset, fileName, fileExtension }
// Actual: undefined or error
```

### Expected behavior

The `contentInfo()` method should parse the Content-Type and Content-Disposition headers and return an object containing:
- MIME type information (type, format, charset)
- File information (name, extension) when Content-Disposition is present

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

This seems like it might have been introduced in a recent change to the response handling code. The method was working fine before but now appears incomplete.

---
Repository: /testbed
