# Bug Report

### Describe the bug

When building a bundle with a global output format and using the `globals` option, the global name resolution is not working correctly. The function appears to return `undefined` even when a valid global name is provided, and the warning for missing global names is not being logged when it should be.

### Reproduction

```js
const rollup = require('rollup');

const bundle = await rollup.rollup({
  input: 'src/index.js',
  external: ['react']
});

await bundle.generate({
  format: 'iife',
  globals: {
    'react': 'React'
  }
});
```

In this case, even though I've specified that the external module `'react'` should use the global name `'React'`, the generated output doesn't use the correct global name. It seems like the global name mapping is being ignored.

### Expected behavior

The bundle should use the provided global name from the `globals` option. When a global name is specified, it should be used in the output. If a global name is missing for an external module with exports, a warning should be logged.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
