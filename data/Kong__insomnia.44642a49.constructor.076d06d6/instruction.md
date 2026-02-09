# Bug Report

### Describe the bug

After a recent update, environment variables with nested objects are being flattened with dot notation instead of preserving their original structure. This is causing issues when trying to access nested properties in the environment.

### Reproduction

```js
const env = new Environment('test', {
  api: {
    baseUrl: 'https://example.com',
    timeout: 5000
  }
});

// Expected: env.get('api') returns the nested object
// Actual: env.get('api') returns undefined
// The values are now accessible as env.get('api.baseUrl') and env.get('api.timeout')
```

### Expected behavior

When creating an Environment with a nested object, the structure should be preserved. Accessing `env.get('api')` should return the nested object `{ baseUrl: 'https://example.com', timeout: 5000 }`, not undefined.

The current behavior forces us to use dot notation (`api.baseUrl`) instead of being able to access the nested structure directly, which breaks existing code that expects nested objects.

### System Info
- Package: insomnia-sdk
- Version: latest

---
Repository: /testbed
