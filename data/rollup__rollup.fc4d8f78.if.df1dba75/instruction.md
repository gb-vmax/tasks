# Bug Report

### Describe the bug

When building IIFE bundles with both `extend: true` and `namedExportsMode: true`, the output is incorrectly assigning the module to a variable/property. The wrapper initialization seems to be missing the assignment operator in certain configurations.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'iife',
    name: 'MyLibrary',
    extend: true,
    exports: 'named'
  }
}
```

When both `extend` and named exports are enabled, the generated IIFE wrapper doesn't properly assign the result. The assignment statement appears to be malformed or missing.

### Expected behavior

The IIFE should correctly assign the module to the specified name regardless of the combination of `extend` and `namedExportsMode` options. The generated code should have proper variable assignment syntax.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
