# Bug Report

### Describe the bug

After a recent update, environment variable interpolation seems to be caching results incorrectly. When I update an environment variable value and try to use `replaceIn()` with the same template string, it returns the old cached value instead of interpolating with the new variable values.

### Reproduction

```js
const env = new Environment();

// Set initial value
env.set('apiUrl', 'https://dev.example.com');
let result1 = env.replaceIn('{{apiUrl}}/users');
console.log(result1); // Outputs: https://dev.example.com/users

// Update the variable
env.set('apiUrl', 'https://prod.example.com');
let result2 = env.replaceIn('{{apiUrl}}/users');
console.log(result2); // Still outputs: https://dev.example.com/users (WRONG!)
```

### Expected behavior

The second call to `replaceIn()` should return `https://prod.example.com/users` with the updated environment variable value, not the cached result from the first call.

### Additional context

This is causing issues in my workflow where I need to switch between different environments dynamically. The interpolation results seem to be cached based on the template string alone, without considering that the underlying environment variable values might have changed.

---
Repository: /testbed
