# Bug Report

### Describe the bug

Environment variables are not being loaded correctly. When creating an `Environment` object with a JSON object containing key-value pairs, the environment appears to be empty and none of the variables are accessible.

### Reproduction

```js
const envData = {
  API_URL: 'https://api.example.com',
  API_KEY: 'secret123',
  TIMEOUT: 5000
};

const env = new Environment('production', envData);

// Variables are not accessible
console.log(env.get('API_URL')); // Expected: 'https://api.example.com', Actual: undefined
console.log(env.get('API_KEY')); // Expected: 'secret123', Actual: undefined
```

### Expected behavior

The environment should contain all the key-value pairs passed in the `jsonObject` parameter during construction. All variables should be accessible via the environment's methods.

### System Info

- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
