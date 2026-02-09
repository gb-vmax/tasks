# Bug Report

### Describe the bug

Rollup is throwing an error when I try to pass a valid options object. The error message says "You must supply an options object with valid properties to rollup" even though I'm providing all the required configuration.

### Reproduction

```js
const rollup = require('rollup');

const inputOptions = {
  input: 'src/main.js',
  plugins: []
};

// This throws an error unexpectedly
rollup.rollup(inputOptions);
```

The above code throws:
```
Error: You must supply an options object with valid properties to rollup
```

### Expected behavior

The build should proceed normally when a valid options object is provided. This used to work in previous versions.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
