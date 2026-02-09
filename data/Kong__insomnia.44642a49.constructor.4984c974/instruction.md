# Bug Report

### Describe the bug

Environment variables are not being set correctly. When creating an Environment object with key-value pairs, the keys and values appear to be swapped or missing entirely.

### Reproduction

```js
const env = new Environment('test-env', {
  API_KEY: 'secret123',
  BASE_URL: 'https://api.example.com',
  TIMEOUT: 5000
});

// Try to access the variables
console.log(env.get('API_KEY')); // Expected: 'secret123', but getting wrong value or undefined
console.log(env.get('BASE_URL')); // Expected: 'https://api.example.com', but getting wrong value or undefined
```

### Expected behavior

Environment variables should be accessible using their original keys and return their corresponding values. In the example above, `env.get('API_KEY')` should return `'secret123'`.

### Additional context

This seems to have broken recently. Previously environment variables were working fine but now they're either not accessible or returning unexpected values. It's affecting all my API requests that depend on environment configuration.

---
Repository: /testbed
