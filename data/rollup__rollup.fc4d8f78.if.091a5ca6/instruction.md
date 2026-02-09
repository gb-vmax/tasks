# Bug Report

### Describe the bug

I'm experiencing an issue with module inclusion in bundle generation. It appears that modules are not being properly included in the output when they should be. Specifically, modules that are entry points but not explicitly included elsewhere seem to be getting excluded from the final bundle.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/entry.js',
  output: {
    dir: 'dist',
    format: 'es'
  }
}

// src/entry.js (entry module that is not imported elsewhere)
export const value = 42;
```

When building, the entry module should always be included in the bundle output, but it's being excluded unless it's also marked as included through other means.

### Expected behavior

Entry modules should always be included in the bundle regardless of whether they are marked as included through other mechanisms. The condition for including a module should treat entry points as a separate case that guarantees inclusion.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
