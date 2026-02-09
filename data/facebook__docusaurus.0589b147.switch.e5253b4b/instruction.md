# Bug Report

### Describe the bug

When using template literals without expressions for translation labels, they are being incorrectly rejected. Template literals that should be valid (e.g., `` `Hello World` ``) are not being recognized as valid translation strings.

### Reproduction

```js
// This should be valid but is being rejected
const label = `Simple string without any expressions`;

// Basic template literal without ${} should work
translate(`Welcome`);

// This used to work in previous versions
const message = `Static text`;
```

### Expected behavior

Template literals without any expressions should be treated the same as regular string literals for translation purposes. A template literal like `` `Hello` `` contains no expressions and should be considered a valid translation label, just like `'Hello'`.

### Additional context

This appears to be a regression - template literals without interpolation were working correctly before. The validation logic seems to have changed and is now incorrectly handling these cases.

---
Repository: /testbed
