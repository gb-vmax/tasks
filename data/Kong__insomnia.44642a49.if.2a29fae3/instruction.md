# Bug Report

### Describe the bug

When using the plugin API to filter request parameters by name, the filtering doesn't work at all. Instead of returning only the parameters that match the specified name, it returns ALL parameters regardless of the name filter.

### Reproduction

```js
const parameters = [
  { name: 'Authorization', value: 'Bearer token123' },
  { name: 'Content-Type', value: 'application/json' },
  { name: 'X-Custom-Header', value: 'custom-value' }
];

// Try to filter for 'Authorization' only
const filtered = filterParameters(parameters, 'Authorization');

// Expected: [{ name: 'Authorization', value: 'Bearer token123' }]
// Actual: Returns all 3 parameters
console.log(filtered);
```

### Expected behavior

The function should return only the parameters whose name matches the filter string. In the example above, it should return an array with only the Authorization parameter.

### System Info
- Insomnia version: latest
- OS: macOS

This is breaking my plugin that relies on filtering specific headers from requests. Any parameter filtering now returns everything instead of the filtered subset.

---
Repository: /testbed
