# Bug Report

### Describe the bug

The `contentInfo()` method on Response objects appears to be broken and returns incomplete data. When trying to access response content information, the method doesn't return the expected object with mime type, charset, and file information.

### Reproduction

```js
const response = new Response({
  headers: [
    { key: 'Content-Type', value: 'application/json; charset=utf-8' },
    { key: 'Content-Disposition', value: 'attachment; filename="data.json"' }
  ],
  body: '{"test": "data"}'
});

const info = response.contentInfo();
console.log(info);
// Expected: { mimeType: 'application/json', charset: 'utf-8', fileName: 'data', fileExtension: 'json', ... }
// Actual: undefined or incomplete object
```

### Expected behavior

The `contentInfo()` method should parse the Content-Type and Content-Disposition headers correctly and return a complete ResponseContentInfo object containing:
- mimeType
- mimeFormat
- charset
- fileExtension
- fileName
- contentType

### Additional context

This seems to have broken recently. The method was working fine before but now it doesn't return anything useful. Not sure what changed but it's blocking our ability to properly handle response metadata.

---
Repository: /testbed
