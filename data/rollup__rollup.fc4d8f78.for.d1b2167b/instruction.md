# Bug Report

### Describe the bug

When bundling with `preserveModules: false`, external dependencies are not getting their variable names assigned properly. This causes issues where the generated code references undefined variables for external imports.

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
  external: ['some-external-package']
}

// src/index.js
import { something } from 'some-external-package';
export { something };
```

After building, the output bundle references external dependencies but the variable names are not being set, leading to potential conflicts or undefined references in the generated code.

### Expected behavior

External dependencies should have their `variableName` properly assigned regardless of the `preserveModules` setting, ensuring that the generated code can correctly reference external imports.

### System Info

- Rollup version: latest
- Node version: 18.x
- OS: macOS

This seems to have broken recently, as it was working fine in previous versions. The issue only appears when `preserveModules` is set to `false`.

---
Repository: /testbed
