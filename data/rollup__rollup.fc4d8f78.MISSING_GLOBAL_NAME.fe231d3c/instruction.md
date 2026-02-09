# Bug Report

### Describe the bug

When using Rollup with external modules that need global variable names, the warning message for missing global names displays incorrect information. The pluralization logic is wrong (it shows "names" even when there's only one warning), and more importantly, it's showing the wrong guessed global variable name from the array.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  external: ['lodash'],
  output: {
    file: 'dist/bundle.js',
    format: 'iife'
    // Missing output.globals configuration
  }
}
```

When building with an external module that doesn't have a global name specified, the warning message shows:
- Incorrect pluralization ("names" instead of "name" for a single warning)
- Wrong guessed variable name (showing the first element instead of what should be displayed)

### Expected behavior

The warning should:
1. Correctly pluralize based on the number of warnings (singular "name" for 1 warning, plural "names" for multiple)
2. Display the appropriate guessed global variable name for each external module

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
