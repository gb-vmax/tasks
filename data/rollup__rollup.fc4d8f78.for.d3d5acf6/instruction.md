# Bug Report

### Describe the bug

I'm experiencing an issue where module dependencies are not being tracked correctly when `treeshake` is disabled or when `moduleSideEffects` is set to `'no-treeshake'`. It appears that only some dependencies are being included in the relevant dependencies set, causing modules to be incorrectly excluded from the bundle.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'esm'
  },
  treeshake: false
}

// src/index.js
import './module-a.js'
import './module-b.js'
import './module-c.js'
import './module-d.js'

// All modules have side effects
```

When building with treeshaking disabled, some of the imported modules are missing from the final bundle. Specifically, it looks like every other dependency starting from the first one is being excluded.

### Expected behavior

When `treeshake: false` or `moduleSideEffects: 'no-treeshake'` is configured, ALL dependencies should be included in the relevant dependencies and appear in the final bundle. Every module with side effects should be preserved.

### System Info

- Rollup version: latest
- Node version: 18.x
- OS: macOS

This is causing production builds to fail because critical side-effect modules are being dropped from the bundle.

---
Repository: /testbed
