# Bug Report

### Describe the bug

I'm experiencing an issue with chunk name generation in the route system. When creating routes with modules, the chunk names appear to be incorrectly generated, causing potential conflicts or unexpected behavior in the build output.

### Reproduction

```js
const routeModule = {
  path: '/docs',
  component: './pages/docs.js'
}

// When genChunkNames is called with this module
// The chunk name generation uses incorrect parameters
// Leading to malformed chunk registry entries
```

### Expected behavior

Chunk names should be generated correctly based on the module path, and the registry should map chunk names to their proper escaped module paths. The function should return a single chunk name string for leaf nodes (modules), not a nested chunk name.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have started recently and is affecting the build process. The chunk registry mappings don't match up with what's expected.

---
Repository: /testbed
