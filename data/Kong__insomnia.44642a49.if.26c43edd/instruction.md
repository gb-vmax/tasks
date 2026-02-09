# Bug Report

### Describe the bug

After a recent update, the `filterParameters` function is not working as expected. When trying to filter parameters by name, the function returns an empty array even when matching parameters exist.

### Reproduction

```js
const parameters = [
  { name: 'Content-Type', value: 'application/json' },
  { name: 'Authorization', value: 'Bearer token123' },
  { name: 'Accept', value: 'application/json' }
];

// This returns an empty array instead of the matching parameter
const result = filterParameters(parameters, 'Content-Type');
console.log(result); // Expected: [{ name: 'Content-Type', value: 'application/json' }]
                     // Actual: []
```

### Expected behavior

The function should return an array containing all parameters whose name matches the provided string. In the example above, it should return the `Content-Type` parameter.

### Additional context

This seems to have broken after the latest changes. The function is supposed to filter parameters by their name property, but it's now returning empty arrays for all queries, even simple exact matches.

---
Repository: /testbed
