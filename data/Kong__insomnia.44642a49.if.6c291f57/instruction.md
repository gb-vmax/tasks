# Bug Report

### Describe the bug

I'm experiencing an issue with authentication parameter lookup in the SDK. When working with auth configurations that have array values, the first element in the array is being skipped during the search process.

### Reproduction

```js
const auth = {
  oauth2: [
    { key: 'accessToken', value: 'token123' },
    { key: 'clientId', value: 'client456' }
  ]
};

// Trying to retrieve 'accessToken' fails
// The search starts at index 1 instead of 0, so the first element is never checked
```

### Expected behavior

All elements in the array should be checked when searching for a matching key, including the first element at index 0. The function should return the value for 'accessToken' when it exists as the first item in the array.

### Additional context

This appears to affect OAuth2 and other authentication methods that store parameters as arrays of key-value pairs. If the target parameter happens to be the first item in the array, it won't be found even though it exists.

---
Repository: /testbed
