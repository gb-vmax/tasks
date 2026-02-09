# Bug Report

### Describe the bug

The `getContentTypeName` function is returning incorrect content type names when given certain content type strings. It seems to be matching the wrong content types, particularly when there are overlapping or similar content type patterns.

### Reproduction

```js
// Example that demonstrates the issue
const contentType = 'application/json';
const result = getContentTypeName(contentType);

// Expected: Should return the name for 'application/json'
// Actual: Returns a different or unexpected content type name
```

When I pass in a specific content type string like `'application/json'`, the function returns an incorrect or unexpected content type name. This appears to be related to how the function matches content type strings against the available content types in the map.

### Expected behavior

The function should return the correct content type name that matches the given content type string. For example:
- `getContentTypeName('application/json')` should return the name associated with JSON content type
- `getContentTypeName('text/html')` should return the name associated with HTML content type

The matching logic should correctly identify the appropriate content type from the map.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
