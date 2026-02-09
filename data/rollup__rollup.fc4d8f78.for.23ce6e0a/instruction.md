# Bug Report

### Describe the bug

When running rollup with cache enabled in the configuration, the build process doesn't wait for completion before moving on. This causes issues when multiple input options are being processed sequentially, as subsequent builds may start before the previous one finishes.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'es'
  },
  cache: true
}
```

Run the build command:
```
rollup -c
```

### Expected behavior

The build should complete fully and wait for each input option to finish processing before moving to the next one, regardless of whether cache is enabled or not.

### Actual behavior

When cache is enabled in the config, the build doesn't await completion properly, which can lead to race conditions or incomplete builds when processing multiple configurations.

---
Repository: /testbed
