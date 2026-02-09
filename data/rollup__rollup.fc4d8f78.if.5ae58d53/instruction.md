# Bug Report

### Describe the bug

Rollup is throwing an error "You must supply an options object to rollup" even when a valid options object is provided. This makes it impossible to use rollup with any configuration.

### Reproduction

```js
const rollup = require('rollup');

const inputOptions = {
  input: 'src/main.js',
  plugins: []
};

// This throws an error even though options are provided
rollup.rollup(inputOptions);
```

### Expected behavior

Rollup should accept the options object and proceed with bundling. The error should only be thrown when options are NOT provided (null, undefined, etc.).

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have broken in the most recent update. Previously this configuration worked fine.

---
Repository: /testbed
