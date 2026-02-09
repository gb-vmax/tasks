# Bug Report

### Describe the bug

The `validateVersionNames` function is not properly validating the versions file format. When I provide a valid array of version names, it throws an error saying the file should contain an array, even though it already is an array. Conversely, when I provide invalid data (non-array), it doesn't throw any error at all.

### Reproduction

```js
// This should work but throws an error
validateVersionNames(['1.0.0', '2.0.0', '3.0.0'])
// Error: The versions file should contain an array of version names! Found content: ["1.0.0","2.0.0","3.0.0"]

// This should throw an error but doesn't
validateVersionNames({ version: '1.0.0' })
// No error thrown
```

### Expected behavior

The function should:
- Accept valid arrays of version names without throwing errors
- Reject non-array inputs with an appropriate error message

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
