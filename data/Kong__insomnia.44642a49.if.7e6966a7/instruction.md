# Bug Report

### Describe the bug
After a recent update, authentication parameters are no longer being retrieved correctly from request configurations. When trying to access auth values by key, the function seems to be ignoring the actual structure of the data and returns `undefined` instead of the expected values.

### Reproduction
```js
const auth = {
  type: 'bearer',
  bearer: [
    { key: 'token', value: 'my-secret-token' }
  ]
};

// Try to get the token value
const token = getAuthValue(auth, 'token');
// Expected: 'my-secret-token'
// Actual: undefined
```

### Expected behavior
The function should correctly extract authentication values from the configuration object when provided with a valid key. It should handle both simple string values and nested array structures.

### Additional context
This was working fine in the previous version. The auth configuration structure hasn't changed on my end, so this seems like a regression introduced in the latest update.

---
Repository: /testbed
