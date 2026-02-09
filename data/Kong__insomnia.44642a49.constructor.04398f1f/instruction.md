# Bug Report

### Describe the bug
Environment variables with leading/trailing whitespace in their names are not being handled correctly. When setting environment variables with spaces around the name, they should be trimmed automatically, but this doesn't seem to be working as expected.

Additionally, variables that start with double underscores (`__`) are appearing in the environment when they should probably be filtered out (looks like internal/private variables).

### Reproduction
```js
const env = new Environment('test', {
  '  myVar  ': 'value1',
  '__internal': 'value2',
  'normalVar': 'value3'
});

// Expected: only 'myVar' (trimmed) and 'normalVar' should be accessible
// Actual: all three variables are present with their original names
```

### Expected behavior
- Variable names should be automatically trimmed of leading/trailing whitespace
- Variables starting with `__` (double underscore) should be filtered out as they appear to be internal variables

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
