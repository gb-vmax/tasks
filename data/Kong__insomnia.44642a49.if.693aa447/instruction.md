# Bug Report

### Describe the bug

When validating environment variable keys, empty strings or keys containing only whitespace are now being rejected with an error message. Previously, these keys were allowed through validation.

### Reproduction

```js
// This now fails validation but used to pass
const result = ensureKeyIsValid('', true);
// Returns: "Key cannot be empty or contain only whitespace"

// Same issue with whitespace-only keys
const result2 = ensureKeyIsValid('   ', false);
// Returns: "Key cannot be empty or contain only whitespace"
```

### Expected behavior

Empty or whitespace-only keys should be handled the same way they were before - either allowed through or validated consistently with the previous behavior. This is causing issues when working with environment variables that may have been created with empty keys in older versions.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
