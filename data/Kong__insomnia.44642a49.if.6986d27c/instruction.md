# Bug Report

### Describe the bug

After a recent update, the plugin context request filtering is broken. When trying to filter request parameters by name, I'm getting duplicate results or no results at all depending on the input.

### Reproduction

```js
// This used to work fine but now returns unexpected results
const params = [
  { name: 'Authorization', value: 'Bearer token' },
  { name: 'Content-Type', value: 'application/json' }
];

const filtered = filterParameters(params, 'Authorization');
// Expected: [{ name: 'Authorization', value: 'Bearer token' }]
// Actual: Returns empty array or duplicates
```

### Expected behavior

The `filterParameters` function should return only the parameters that match the given name, just like it did before. Right now it seems like the filtering logic is completely broken.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
