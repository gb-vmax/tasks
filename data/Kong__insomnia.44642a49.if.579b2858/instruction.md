# Bug Report

### Describe the bug

When creating authentication configurations with duplicate variable keys, all duplicates are preserved instead of being deduplicated. This can lead to unexpected behavior where the same authentication parameter appears multiple times with potentially different values, and it's unclear which value will be used.

### Reproduction

```js
const auth = new Auth({
  type: 'bearer',
  bearer: [
    { key: 'token', value: 'first-token' },
    { key: 'token', value: 'second-token' },
    { key: 'token', value: 'third-token' }
  ]
});

// Expected: Only one 'token' variable
// Actual: All three 'token' variables are preserved
```

Similarly, when using VariableList directly:

```js
const vars = new VariableList(undefined, [
  new Variable({ key: 'apiKey', value: 'value1' }),
  new Variable({ key: 'apiKey', value: 'value2' })
]);

// Both variables with key 'apiKey' exist in the list
```

### Expected behavior

When duplicate keys are present in authentication options or variable lists, only the last occurrence should be kept (or some consistent deduplication strategy should be applied). This would prevent ambiguity about which value will actually be used during authentication.

### Additional context

This also affects variables with empty or whitespace-only keys, which probably shouldn't be included in the final variable list at all.

---
Repository: /testbed
