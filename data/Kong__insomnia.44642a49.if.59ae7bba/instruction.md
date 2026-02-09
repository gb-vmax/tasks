# Bug Report

### Describe the bug

I'm experiencing an issue with authentication configuration where variables with empty keys or null/undefined values are being accepted and processed. This causes problems when trying to use the auth configuration, as invalid variables shouldn't be allowed in the first place.

Additionally, when I define multiple variables with the same key, all of them are being kept instead of only keeping the last one (which would be the expected behavior for overriding values).

### Reproduction

```js
const auth = {
  type: 'bearer',
  bearer: [
    { key: '', value: 'should-be-filtered' },
    { key: 'token', value: null },
    { key: 'valid', value: 'test-value' },
    { key: 'duplicate', value: 'first' },
    { key: 'duplicate', value: 'second' }
  ]
}

// Currently all variables are processed, including:
// - Empty key variables
// - Variables with null/undefined values
// - Duplicate keys (both 'first' and 'second' are kept)
```

### Expected behavior

The auth system should:
1. Filter out variables with empty/whitespace-only keys
2. Filter out variables with null or undefined values
3. Deduplicate variables by key (keeping only the last occurrence)

This would prevent invalid configurations from being processed and ensure cleaner auth variable handling.

### System Info
- insomnia-sdk version: latest
- Environment: Node.js

---
Repository: /testbed
