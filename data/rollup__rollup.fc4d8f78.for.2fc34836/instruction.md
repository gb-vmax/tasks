# Bug Report

### Describe the bug

When using `treeshake: false` or `moduleSideEffects: 'no-treeshake'`, some module dependencies are not being included in the bundle. This causes runtime errors when the bundled code tries to access imports from these missing dependencies.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/main.js',
  output: {
    file: 'dist/bundle.js',
    format: 'esm'
  },
  treeshake: false
}

// src/main.js
import dep1 from './dep1.js'
import dep2 from './dep2.js'
import dep3 from './dep3.js'
import dep4 from './dep4.js'

console.log(dep1, dep2, dep3, dep4)
```

After bundling, only some of the dependencies (dep1, dep3) are included in the output, while others (dep2, dep4) are missing, causing the bundle to fail at runtime.

### Expected behavior

When treeshaking is disabled, ALL dependencies should be included in the bundle regardless of whether they appear to be used or not. Currently it seems like only every other dependency is being preserved.

### System Info

- Rollup version: latest
- Node version: 18.x
- OS: macOS

This is breaking our production builds where we intentionally disable treeshaking for certain modules that have side effects.

---
Repository: /testbed
