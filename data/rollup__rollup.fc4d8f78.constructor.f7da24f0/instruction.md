# Bug Report

### Describe the bug
When using watch mode with multiple configurations that have different `buildDelay` values, the watcher seems to use an incorrect delay. I expected it to use the maximum delay from all configurations, but it appears to be using the minimum instead.

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
    input: 'src/other.js',
    output: { file: 'dist/bundle2.js' },
    watch: {
      buildDelay: 500
    }
  }
]
```

When running in watch mode, the effective build delay is 500ms instead of the expected 1000ms. This causes builds to trigger too quickly when I make rapid changes to files.

### Expected behavior
The watcher should use the largest `buildDelay` value from all configurations (1000ms in this example) to ensure all builds have adequate debounce time.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
