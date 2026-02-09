# Bug Report

### Describe the bug

When enabling performance timing with `perf: true`, the timer functions are not working as expected. The timing measurements appear to be completely disabled even though performance tracking is explicitly enabled in the configuration.

### Reproduction

```js
const rollup = require('rollup');

const bundle = await rollup.rollup({
  input: 'src/main.js',
  perf: true,  // Performance timing enabled
  plugins: [
    // ... your plugins
  ]
});

// Expected: Performance timings should be collected and available
// Actual: No timing data is being recorded
```

### Expected behavior

When `perf: true` is set in the input options, the build process should collect and display performance timing information for various build phases and plugin operations. The timer functions should be active and recording data.

### System Info

- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
