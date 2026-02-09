# Bug Report

### Describe the bug

After a recent update, authentication variables are being processed incorrectly. When setting up auth with duplicate keys or empty/whitespace keys, the variables aren't being handled properly and it's causing issues with request authentication.

### Reproduction

```js
const auth = new Auth({
  type: 'bearer',
  bearer: [
    { key: 'token', value: 'abc123' },
    { key: 'token', value: 'xyz789' },  // duplicate key
    { key: '  ', value: 'should-be-ignored' },  // whitespace key
    { key: '', value: 'also-ignored' }  // empty key
  ]
});

// Expected: Only one 'token' variable with proper deduplication
// Expected: Empty/whitespace keys should be filtered out
// Actual: Duplicate keys are kept, empty keys cause problems
```

Also seeing issues when using VariableList directly:

```js
const variables = new VariableList(undefined, [
  new Variable({ key: 'apiKey', value: 'test1' }),
  new Variable({ key: 'apiKey', value: 'test2' }),  // duplicate
]);

// Variables aren't being deduplicated
```

### Expected behavior

- Duplicate variable keys should be deduplicated (last one wins)
- Variables with empty, null, or whitespace-only keys should be filtered out
- Variable values should be properly sanitized and converted to strings

### System Info

- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
