# Bug Report

### Describe the bug

When using the `experimentalLogSideEffects` option, side effects are not being logged to the console. The first side effect in the code should trigger a log message, but nothing appears in the output.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'esm'
  },
  experimentalLogSideEffects: true
}

// src/index.js
console.log('This should be logged as a side effect');
const x = 10;
```

### Expected behavior

The bundler should log information about the first side effect detected (the `console.log` statement) when `experimentalLogSideEffects` is enabled. The log should include the location and details of where the side effect occurs in the source code.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
