# Bug Report

### Describe the bug

When using the `--clearScreen` flag (or `clearScreen` option) in watch mode, the screen clearing behavior is not respecting the configuration correctly. If I explicitly set `clearScreen: false` in my rollup config, the screen still gets cleared on rebuilds.

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

Run with watch mode and trigger a rebuild - the screen gets cleared even though `clearScreen` is explicitly set to `false`.

### Expected behavior

When `clearScreen: false` is set in the watch configuration, the screen should NOT be cleared between rebuilds. The previous output should remain visible in the terminal.

### Additional context

This seems to affect scenarios where you want to keep the terminal history visible, for example when debugging or when you have other processes logging to the same terminal.

---
Repository: /testbed
