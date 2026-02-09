# Bug Report

### Describe the bug

When setting authentication parameters with duplicate keys or null/undefined values, the auth configuration doesn't handle them properly. This leads to unexpected behavior where duplicate keys aren't deduplicated and null/undefined values aren't normalized to empty strings.

### Reproduction

```js
const authVars = new VariableList(undefined, [
  new Variable({ key: 'username', value: 'user1' }),
  new Variable({ key: 'username', value: 'user2' }),  // duplicate key
  new Variable({ key: 'password', value: null }),      // null value
  new Variable({ key: 'token', value: undefined })     // undefined value
]);

// Pass to auth configuration
const auth = new RequestAuth({
  type: 'basic',
  basic: authVars
});

// Expected: Only one 'username' entry (last one wins), null/undefined converted to ''
// Actual: Both username entries present, null/undefined not normalized
```

Also happens when using the array format:

```js
const authOptions = [
  { key: 'apiKey', value: 'key1' },
  { key: 'apiKey', value: 'key2' },  // duplicate
  { key: 'secret', value: null }
];

// Same issue - duplicates not removed, null not normalized
```

### Expected behavior

- Duplicate keys should be deduplicated (keeping the last occurrence)
- Null and undefined values should be normalized to empty strings
- Empty or whitespace-only keys should be filtered out

### System Info

- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
