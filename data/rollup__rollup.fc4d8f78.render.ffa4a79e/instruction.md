# Bug Report

### Describe the bug

When using dynamic imports with inlined namespaces, the generated code includes an extra character at the beginning that breaks the output. The resulting code is malformed and causes syntax errors.

### Reproduction

```js
// Input code with dynamic import
import('./module.js')

// When the namespace is inlined, the output becomes:
iPromise.resolve().then(...)
// Notice the extra 'i' at the start
```

The generated code should start with `Promise.resolve()` but instead has an extra character prepended, making it invalid JavaScript.

### Expected behavior

Dynamic imports with inlined namespaces should be replaced with valid `Promise.resolve().then(...)` calls without any extra characters at the beginning.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
