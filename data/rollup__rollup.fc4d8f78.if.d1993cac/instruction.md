# Bug Report

### Describe the bug

When generating IIFE bundles with namespaced names (e.g., `MyLib.Core`), the output is broken. The namespace setup code is not being included in the wrapper, causing the generated bundle to fail at runtime.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    format: 'iife',
    name: 'MyApp.Utils',
    file: 'dist/bundle.js'
  }
}
```

When building with a namespaced name like `MyApp.Utils`, the generated IIFE doesn't properly set up the namespace object structure. The output tries to assign to `MyApp.Utils` without first ensuring that `MyApp` exists, resulting in a runtime error:

```
Uncaught TypeError: Cannot set property 'Utils' of undefined
```

### Expected behavior

The bundle should properly initialize the namespace hierarchy before assigning the module. Non-namespaced names (like `MyApp`) work fine, but any nested namespace fails.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
