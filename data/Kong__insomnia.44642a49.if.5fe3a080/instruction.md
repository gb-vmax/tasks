# Bug Report

### Describe the bug

I'm experiencing an issue where authentication parameters are not being retrieved correctly when using nested key-value structures. It seems like the lookup function is not properly traversing nested objects to find the target key.

### Reproduction

```js
const auth = {
  type: 'oauth2',
  oauth2: [
    {
      key: 'credentials',
      value: {
        accessToken: 'my-token-123'
      }
    }
  ]
};

// Trying to retrieve 'accessToken' from nested structure
// Expected: 'my-token-123'
// Actual: undefined
```

When the authentication configuration has nested objects within arrays, the key lookup fails to find values that are deeply nested. The function only checks the immediate level and doesn't recursively search through nested objects.

### Expected behavior

The authentication lookup should recursively search through nested structures to find the target key, regardless of how deeply it's nested within the configuration object.

### System Info
- Package: insomnia-sdk
- Node version: 18.x

---
Repository: /testbed
