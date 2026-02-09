# Bug Report

### Describe the bug

When using watch mode with `clearScreen: false` in the configuration, the screen is still being cleared during rebuilds. The configuration option seems to be ignored and the terminal gets cleared anyway.

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

Run rollup in watch mode and make a change to trigger a rebuild. The screen clears even though `clearScreen` is explicitly set to `false`.

### Expected behavior

When `watch.clearScreen` is set to `false`, the terminal should not be cleared between rebuilds. Previous output should remain visible.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
