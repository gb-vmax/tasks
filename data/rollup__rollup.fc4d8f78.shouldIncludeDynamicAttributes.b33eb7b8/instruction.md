# Bug Report

### Describe the bug

Dynamic import attributes are not being included in the output even when they should be. When using dynamic imports with attributes like `assert` or `with`, the attributes are being stripped from the generated code unexpectedly.

### Reproduction

```js
// Input code
const module = import('./module.json', { 
  assert: { type: 'json' } 
});

// Expected output should preserve the import attributes
// But they're being removed from the bundle
```

Another case:

```js
import('./data.json', { 
  with: { type: 'json' } 
})
```

The import attributes disappear in the bundled output when they should be preserved.

### Expected behavior

Dynamic import attributes should be included in the output when specified in the source code. The bundler should respect the `assert` and `with` clauses for dynamic imports.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
