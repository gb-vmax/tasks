# Bug Report

### Describe the bug

Performance timing is completely broken - when I enable the `perf` option, timing functions don't work at all and nothing gets measured. Conversely, when `perf` is disabled, the timers seem to be active when they shouldn't be.

### Reproduction

```js
const rollup = require('rollup');

// Enable performance tracking
const bundle = await rollup.rollup({
  input: 'src/main.js',
  perf: true,
  plugins: [/* ... */]
});

// Expected: timing data should be collected
// Actual: no timing information is available
```

When I set `perf: true`, I expect to see performance measurements, but the timing functions appear to be no-ops. When I set `perf: false` or omit it entirely, it seems like timing is actually enabled instead.

### Expected behavior

- When `perf: true` is set, performance timers should be active and collect timing data
- When `perf: false` or perf is not specified, timing functions should be no-ops

### System Info
- rollup version: latest
- Node.js: v18.x

---
Repository: /testbed
