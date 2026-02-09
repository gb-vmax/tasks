# Bug Report

### Describe the bug

When configuring multiple watch options with different `buildDelay` values, the watcher is using the shortest delay instead of the longest one. This causes builds to trigger too quickly when you have multiple configurations with different delay requirements.

### Reproduction

```js
// rollup.config.js
export default [
  {
    input: 'src/main.js',
    output: { file: 'dist/bundle1.js' },
    watch: {
      buildDelay: 1000
    }
  },
  {
    input: 'src/secondary.js',
    output: { file: 'dist/bundle2.js' },
    watch: {
      buildDelay: 500
    }
  }
]
```

With this configuration, the watcher uses a 500ms delay instead of the expected 1000ms. The build triggers after only 500ms when files change, which is too fast for the first configuration's requirements.

### Expected behavior

The watcher should respect the maximum `buildDelay` across all configurations to ensure all builds have adequate time before triggering. In the example above, it should use 1000ms as the delay.

### Additional context

This seems to have changed recently. Previously the watcher would wait for the longest delay to accommodate all configurations properly.

---
Repository: /testbed
