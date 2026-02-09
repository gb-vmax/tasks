# Bug Report

### Describe the bug

I'm experiencing an issue with authentication variables where duplicate keys are appearing in the variable list. When I set up auth configuration with multiple variables that have the same key, all duplicates are being preserved instead of only keeping the last occurrence.

### Reproduction

```js
const authVars = new VariableList(undefined, [
  new Variable({ key: 'username', value: 'user1' }),
  new Variable({ key: 'password', value: 'pass1' }),
  new Variable({ key: 'username', value: 'user2' }), // duplicate key
]);

// Pass this to auth configuration
const auth = new RequestAuth({
  type: 'basic',
  basic: authVars
});

// Expected: only one 'username' variable with value 'user2'
// Actual: both username variables are present
```

The same issue occurs when using `AuthOptions` objects with arrays containing duplicate keys:

```js
const authOptions = {
  basic: [
    { key: 'token', value: 'abc123' },
    { key: 'token', value: 'xyz789' }
  ]
};
```

### Expected behavior

When there are multiple variables with the same key, only the last one should be kept (similar to how object properties work in JavaScript). The variable list should automatically deduplicate based on the key name.

### System Info
- insomnia-sdk version: latest
- This affects all auth types (basic, bearer, oauth, etc.)

---
Repository: /testbed
