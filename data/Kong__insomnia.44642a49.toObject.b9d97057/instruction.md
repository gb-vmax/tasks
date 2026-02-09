# Bug Report

### Describe the bug

I'm experiencing an issue with environment variable interpolation in the SDK. When trying to use variables in my requests, the interpolation seems to return incorrect data structure. Instead of getting the actual key-value pairs from the environment, I'm getting something that looks like an array of keys only.

### Reproduction

```js
const env = new Environment();
env.set('api_key', 'my-secret-key');
env.set('base_url', 'https://api.example.com');

// Try to get the environment object
const envObj = env.toObject();
console.log(envObj);
// Expected: { api_key: 'my-secret-key', base_url: 'https://api.example.com' }
// Actual: Something like [['api_key'], ['base_url']] or similar array structure
```

When I try to use the environment variables in a template:
```js
const template = '{{ base_url }}/users';
const result = env.replaceIn(template);
// This doesn't interpolate correctly anymore
```

### Expected behavior

The `toObject()` method should return a proper object with key-value pairs from the environment, so that template interpolation works correctly. Variables should be properly substituted in templates.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

This seems to have started recently, possibly after a recent update. The environment variables are being set correctly but something is wrong with how they're being converted to an object for interpolation.

---
Repository: /testbed
