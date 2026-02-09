# Bug Report

### Describe the bug

After a recent update, the parameter filtering functionality appears to be broken. When trying to filter parameters by name, I'm getting duplicate results or the filter isn't working at all.

### Reproduction

```js
const parameters = [
  { name: 'Authorization', value: 'Bearer token123' },
  { name: 'Content-Type', value: 'application/json' },
  { name: 'Accept', value: 'application/json' }
];

// Trying to filter by exact name
const filtered = filterParameters(parameters, 'Authorization');
console.log(filtered);
// Expected: [{ name: 'Authorization', value: 'Bearer token123' }]
// Actual: Returns all parameters or unexpected results
```

### Expected behavior

The `filterParameters` function should return only the parameters that match the provided name exactly. Currently it seems like the filtering logic is not working correctly and returns incorrect results.

### Additional context

This is blocking our ability to properly filter request headers and query parameters in plugin development. The function used to work fine before but now the behavior is inconsistent.

---
Repository: /testbed
