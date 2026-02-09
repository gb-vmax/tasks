# Bug Report

### Describe the bug
The `toKebabCase` function is now removing special characters and converting strings in an unexpected way. After a recent update, strings that previously worked are now being transformed incorrectly, breaking functionality that depends on preserving certain characters.

### Reproduction
```js
// These transformations are now different than before
toKebabCase('my string')  // Expected: 'my-string', but special chars get stripped
toKebabCase('api/endpoint')  // The slash gets converted to dash
toKebabCase('test_value')  // Underscores are now converted to dashes
toKebabCase('some.property')  // Dots are being replaced
```

### Expected behavior
The function should only replace spaces with dashes, like it did before. Other characters should be preserved as-is to maintain backwards compatibility with existing code.

### Additional context
This is causing issues in our codebase where we rely on `toKebabCase` to simply convert spaces to dashes without modifying other characters. The new behavior is too aggressive and breaks existing functionality.

---
Repository: /testbed
