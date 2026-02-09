# Bug Report

### Describe the bug

When passing an array of entry points to the bundler, the first entry module is being skipped and not included in the build output. Only the second and subsequent entries are processed correctly.

### Reproduction

```js
const rollup = require('rollup');

const bundle = await rollup.rollup({
  input: ['src/main.js', 'src/secondary.js', 'src/third.js']
});

// Only 'src/secondary.js' and 'src/third.js' are bundled
// 'src/main.js' is missing from the output
```

### Expected behavior

All entry modules provided in the array should be included in the bundle. The first entry (`src/main.js` in the example above) should not be ignored.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
