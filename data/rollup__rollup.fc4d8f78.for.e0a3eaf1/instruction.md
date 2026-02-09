# Bug Report

### Describe the bug
When running rollup with multiple input configurations, the first configuration is being skipped and not built. Only configurations starting from index 1 onwards are being processed.

### Reproduction
```js
// rollup.config.js
export default [
  {
    input: 'src/main.js',
    output: { file: 'dist/main.js', format: 'es' }
  },
  {
    input: 'src/secondary.js',
    output: { file: 'dist/secondary.js', format: 'es' }
  }
]
```

Run the build command - only `dist/secondary.js` gets created, `dist/main.js` is missing.

### Expected behavior
All configurations in the array should be built, including the first one. Both `dist/main.js` and `dist/secondary.js` should be generated.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
