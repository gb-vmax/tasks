# Bug Report

### Describe the bug

I'm experiencing an issue with environment variable validation. The editor is incorrectly rejecting valid keys and allowing reserved keys that should be blocked.

### Reproduction

When trying to set environment variables:

1. Setting a key named `_` (the reserved Nunjucks template global property) at the root level is now allowed when it should be rejected
2. Any non-reserved key in a nested environment throws an error saying it's a reserved key, even though it's not

Example scenario:
```js
// This should be rejected but isn't:
// Root level, key = "_"
// Expected: Error message
// Actual: No error, key is accepted

// This should be accepted but isn't:
// Nested level, key = "myVariable"
// Expected: No error
// Actual: Error: "_" is a reserved key
```

### Expected behavior

- The reserved key `_` should only be blocked at the root level
- Non-reserved keys should be allowed regardless of nesting level
- The validation logic should correctly identify when a key matches the reserved property name

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
