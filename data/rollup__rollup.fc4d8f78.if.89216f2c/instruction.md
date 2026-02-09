# Bug Report

### Describe the bug

When passing an array of entry modules to the bundler, only the modules after the first one are being processed. The first entry point in the array is being completely skipped, which breaks builds that rely on the first entry being included.

### Reproduction

```js
const rollup = require('rollup');

const bundle = await rollup.rollup({
  input: ['src/main.js', 'src/secondary.js', 'src/third.js']
});

// Only 'src/secondary.js' and 'src/third.js' are included in the bundle
// 'src/main.js' is missing from the output
```

### Expected behavior

All entry modules in the array should be processed and included in the bundle. The first entry point (`src/main.js` in the example above) should not be skipped.

### Additional context

This seems to have started happening recently. When I specify a single entry point it works fine, but as soon as I use an array with multiple entries, the first one gets dropped. This is breaking our multi-entry build configuration.

---
Repository: /testbed
