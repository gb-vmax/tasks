# Bug Report

### Describe the bug

When validating environment variable keys, the function is not properly detecting keys that start with '$' or contain '.'. The validation seems to have broken and keys that should be rejected are not being caught correctly.

### Reproduction

```js
// These keys should be invalid but are passing validation
const key1 = '$myvar';
const key2 = 'my.var';

// The validation function should return an error message but doesn't
const result1 = ensureKeyIsValid(key1, false);
const result2 = ensureKeyIsValid(key2, false);

// Expected: error messages
// Actual: null (no error)
```

### Expected behavior

Keys that start with '$' or contain '.' should be rejected with appropriate error messages:
- `"$myvar"` should return an error like `"$myvar" cannot begin with '$'`
- `"my.var"` should return an error like `"my.var" cannot contain a '.'`

### System Info
- Insomnia version: latest
- OS: macOS

This is causing issues when trying to save environment variables with invalid characters - they're being accepted when they shouldn't be, which leads to problems later when trying to use them.

---
Repository: /testbed
