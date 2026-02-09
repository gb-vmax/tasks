# Bug Report

### Describe the bug

After a recent update, the `filterParameters` function seems to have broken. When trying to filter request parameters by name, I'm getting duplicate code that causes syntax errors. The function appears to have been modified but the old implementation wasn't properly removed, resulting in malformed code.

### Reproduction

```js
// Attempting to use filterParameters
const params = [
  { name: 'Authorization', value: 'Bearer token' },
  { name: 'Content-Type', value: 'application/json' }
];

const filtered = filterParameters(params, 'Authorization');
// This should return the matching parameter but the code won't even parse
```

### Expected behavior

The function should filter parameters by name (exact match, wildcard, or regex) and return the matching results. The code should be syntactically valid and executable.

### Additional context

Looking at the code, it seems like there's a duplicate function definition and the old filter logic at the bottom wasn't removed when the new implementation was added. This causes parsing errors before any filtering can even happen.

---
Repository: /testbed
