# Bug Report

### Describe the bug

I'm experiencing an issue with chunk name generation in routes. After a recent update, the chunk names being generated don't match what's expected, and it seems like the wrong values are being returned and stored in the registry.

### Reproduction

When defining routes with modules, the chunk name generation appears to be broken. Instead of getting properly generated chunk names, I'm getting raw module paths back.

For example:
```js
const routes = [
  {
    path: '/docs',
    component: './pages/Docs.js'
  }
]
```

The expected chunk name should be something like `docs-123` but instead it's returning the module path directly.

### Expected behavior

The `genChunkNames` function should:
1. Generate a proper chunk name using the `genChunkName` helper
2. Store the mapping in the registry with the chunk name as the key
3. Return the generated chunk name (not the module path)

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is causing issues with code splitting and chunk loading in production builds. The chunks can't be properly resolved because the registry keys don't match what's being returned.

---
Repository: /testbed
