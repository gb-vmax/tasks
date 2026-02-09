# Bug Report

### Describe the bug

I'm experiencing an issue with namespace member access in my project. When trying to access exported members from a namespace through multiple levels of property access, the bundler gets stuck in what appears to be an infinite loop or recursion.

### Reproduction

```js
// namespace.js
export const config = {
  settings: {
    value: 42
  }
}

// main.js
import * as ns from './namespace.js'
console.log(ns.config.settings.value)
```

When bundling this code, the process hangs and eventually crashes or times out. It seems like the namespace resolution is not progressing through the property path correctly.

### Expected behavior

The bundler should successfully resolve the nested namespace member access and complete the build without hanging. The property path should be traversed step by step until the final member is resolved.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
