# Bug Report

### Describe the bug
When building a project with `moduleSideEffects: 'no-treeshake'`, some dependencies are randomly missing from the output bundle. This causes runtime errors where modules that should be included are not present.

### Reproduction
```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'esm'
  },
  treeshake: false,
  moduleContext: (id) => {
    return {
      moduleSideEffects: 'no-treeshake'
    }
  }
}

// src/index.js
import './dep1.js'
import './dep2.js'
import './dep3.js'
import './dep4.js'

// Expected: all 4 dependencies should be in the bundle
// Actual: only dep1 and dep3 are included (every other one is missing)
```

### Expected behavior
All dependencies should be included in the bundle when treeshaking is disabled or when `moduleSideEffects` is set to `'no-treeshake'`. Every dependency imported should appear in the final output.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

This seems to affect every other dependency in a consistent pattern. Not sure if this is related to recent changes in dependency resolution logic.

---
Repository: /testbed
