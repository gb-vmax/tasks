# Bug Report

### Describe the bug

When using the `watch.clearScreen` configuration option, setting it to `false` doesn't prevent screen clearing as expected. The screen still gets cleared during watch mode even when explicitly configured not to.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'es'
  },
  watch: {
    clearScreen: false
  }
}
```

Run rollup in watch mode with the above config. The terminal screen still clears on rebuild even though `clearScreen` is set to `false`.

### Expected behavior

When `watch.clearScreen` is explicitly set to `false`, the terminal screen should not be cleared between rebuilds in watch mode. The output from previous builds should remain visible.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
