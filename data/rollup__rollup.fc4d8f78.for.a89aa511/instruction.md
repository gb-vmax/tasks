# Bug Report

### Describe the bug

When using external chunks with `preserveModules: false`, the variable names for dependencies are not being set correctly. The deconfliction process seems to be skipping external dependencies unless `preserveModules` is enabled, which causes issues when the same external module is imported multiple times.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    dir: 'dist',
    format: 'esm',
    preserveModules: false
  },
  external: ['lodash']
}

// src/index.js
import _ from 'lodash';
import { map } from 'lodash';

// The external dependency variable name is not properly deconflicted
```

### Expected behavior

External dependencies should have their variable names properly deconflicted regardless of the `preserveModules` setting. The generated code should use unique variable names for each import to avoid naming conflicts.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
