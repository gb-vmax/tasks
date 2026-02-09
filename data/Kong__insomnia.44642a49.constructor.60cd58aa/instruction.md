# Bug Report

### Describe the bug

After a recent update, environment variables with nested objects are being flattened with dot notation keys instead of maintaining their original structure. This is causing issues when trying to access nested properties in the environment.

### Reproduction

```js
const env = new Environment('test', {
  api: {
    endpoint: 'https://example.com',
    timeout: 5000
  }
});

// Expected: env.get('api') returns the nested object
// Actual: env.get('api') returns undefined
// The values are now stored as 'api.endpoint' and 'api.timeout' instead
```

When I create an environment with nested objects like the example above, I can no longer access the parent object. The environment is automatically flattening the structure, so `api.endpoint` and `api.timeout` become separate keys instead of being nested under `api`.

### Expected behavior

The environment should preserve the original object structure. If I pass in a nested object, I should be able to access it as a nested object, not as flattened dot-notation keys.

This is breaking existing workflows where we rely on accessing grouped configuration values.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
