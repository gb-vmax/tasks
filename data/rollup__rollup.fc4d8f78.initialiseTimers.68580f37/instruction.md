# Bug Report

### Describe the bug

When performance monitoring is disabled (`perf: false`), plugins are still being wrapped with timer instrumentation. This causes unnecessary overhead and potentially breaks plugin behavior since the timer wrapping logic is being applied even when timers aren't initialized.

### Reproduction

```js
const rollup = require('rollup');

const build = await rollup.rollup({
  input: 'src/main.js',
  perf: false,  // Performance monitoring disabled
  plugins: [
    myCustomPlugin()
  ]
});
```

With `perf: false`, the plugins still go through `getPluginWithTimers()` which wraps them with timing logic, but the `timers` Map is never initialized. This can lead to unexpected behavior or errors when the wrapped plugin methods try to access timing functionality.

### Expected behavior

When `perf: false`, plugins should not be wrapped with timer instrumentation at all. The `getPluginWithTimers` mapping should only happen when performance monitoring is explicitly enabled.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
