# Bug Report

### Describe the bug

When building with the `output.globals` configuration, chunks without exports are now incorrectly returning their variable name instead of `undefined`. This causes global name assignments to be generated for chunks that shouldn't have them.

### Reproduction

```js
const rollup = require('rollup');

const bundle = await rollup.rollup({
  input: 'entry.js',
  // ... other options
});

await bundle.generate({
  format: 'iife',
  globals: {
    'some-module': 'SomeModule'
  }
});
```

When a chunk has no exports, the global name should be `undefined`, but it's now returning the chunk's variable name instead. This results in unexpected global assignments being created in the output.

### Expected behavior

For chunks without exports:
- Should return `undefined` for the global name
- Should not generate global variable assignments
- Should not log warnings about missing global names

For chunks with exports but no matching global configuration:
- Should log a warning
- Should fall back to using the chunk's variable name

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
