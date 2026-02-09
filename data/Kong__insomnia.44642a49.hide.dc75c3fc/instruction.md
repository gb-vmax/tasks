# Bug Report

### Describe the bug

When using the OS template tag with certain functions, the JSONPath Filter field is not showing up when it should. Specifically, for functions like `networkInterfaces` and `loadavg` that return complex objects, the filter option remains hidden even though these functions would benefit from JSONPath filtering just like `userInfo` and `cpus`.

### Reproduction

```js
// Using the OS template tag
1. Select "networkInterfaces" from the function dropdown
2. Notice that the JSONPath Filter field doesn't appear
3. Same issue occurs with "loadavg" function

// Expected: JSONPath Filter should be visible for these functions since they return objects
// Actual: Filter field remains hidden
```

### Expected behavior

The JSONPath Filter field should be visible for all OS functions that return complex objects/arrays, including:
- `userInfo` (currently works)
- `cpus` (currently works)  
- `networkInterfaces` (not working)
- `loadavg` (not working)

These functions all return structured data that users would want to filter using JSONPath queries.

### System Info
- Insomnia version: latest
- OS: Multiple platforms affected

---
Repository: /testbed
