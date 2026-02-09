# Bug Report

### Describe the bug

When using the `clearScreen` option in watch mode configuration, the screen clearing behavior is not working as expected. Setting `clearScreen: false` in the watch config doesn't prevent the screen from being cleared.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/main.js',
  output: {
    file: 'dist/bundle.js',
    format: 'es'
  },
  watch: {
    clearScreen: false
  }
}
```

When running in watch mode with the above configuration, the screen still gets cleared on rebuilds even though `clearScreen` is explicitly set to `false`.

### Expected behavior

When `watch.clearScreen` is set to `false`, the terminal screen should NOT be cleared between rebuilds. The output from previous builds should remain visible.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
