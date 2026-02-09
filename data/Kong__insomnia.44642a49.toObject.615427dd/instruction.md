# Bug Report

### Describe the bug

When using the `Environment` object and calling `toObject()`, the returned value is not in the expected format. Instead of getting a plain object with key-value pairs, I'm receiving an array containing an object with only keys (no values).

### Reproduction

```js
const env = new Environment();
env.set('API_KEY', 'secret123');
env.set('BASE_URL', 'https://api.example.com');

const obj = env.toObject();
console.log(obj);
// Expected: { API_KEY: 'secret123', BASE_URL: 'https://api.example.com' }
// Actual: [{ API_KEY: undefined, BASE_URL: undefined }] or similar
```

### Expected behavior

The `toObject()` method should return a plain object containing all environment variable key-value pairs, not an array. The values should be preserved when converting to an object.

### Additional context

This is affecting template rendering since `toObject()` is used internally by the `replaceIn()` method. Variables are not being interpolated correctly in templates because the environment data structure is malformed.

---
Repository: /testbed
