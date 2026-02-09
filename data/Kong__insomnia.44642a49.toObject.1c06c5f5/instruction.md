# Bug Report

### Describe the bug

I'm experiencing an issue with environment variables where the first entry in the environment is being skipped. When I set up multiple environment variables, the first one is not accessible in requests or when rendering templates.

### Reproduction

```js
const env = new Environment();
env.set('API_KEY', 'my-secret-key');
env.set('BASE_URL', 'https://api.example.com');
env.set('TIMEOUT', '5000');

const obj = env.toObject();
console.log(obj);
// Expected: { API_KEY: 'my-secret-key', BASE_URL: 'https://api.example.com', TIMEOUT: '5000' }
// Actual: { BASE_URL: 'https://api.example.com', TIMEOUT: '5000' }
// API_KEY is missing!
```

### Expected behavior

All environment variables should be included when converting to an object. The first variable set should not be dropped.

### Additional context

This seems to have started recently. I have several environment variables configured and the first one is consistently missing from the rendered output. This breaks my API authentication since the API_KEY is typically the first variable I define.

---
Repository: /testbed
