# Bug Report

### Describe the bug

I'm experiencing an issue with syntax extension handling in remark. When multiple syntax extensions are registered for the same hook code, the extensions are being completely overwritten instead of being merged together. This causes previously registered extensions to be lost.

### Reproduction

```js
const processor = remark()
  .use(plugin1) // Registers extension for code 'A'
  .use(plugin2) // Also registers extension for code 'A'

// After applying both plugins, only plugin2's extension is active
// plugin1's extension has been overwritten and lost
```

### Expected behavior

When multiple plugins register extensions for the same hook code, they should be combined/merged together so that all registered extensions are active. The second plugin should not completely replace the first plugin's extensions.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
