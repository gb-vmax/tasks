# Bug Report

### Describe the bug

I'm experiencing an issue with route module chunk generation where the logic for handling route modules appears to be inverted. When processing route modules, the system is now attempting to generate chunk names and registry entries for non-module routes instead of actual module routes.

### Reproduction

```js
const routeModule = {
  path: '/docs',
  component: './DocsPage.tsx'
}

// When genChunkNames is called with an actual module
// No chunk name is returned and nothing is registered
const result = genChunkNames(routeModule, 'prefix', 'name', registry)
// result is undefined, but should be a chunk name string
```

### Expected behavior

When `genChunkNames` is called with a module route (leaf node), it should:
1. Generate a chunk name for the module
2. Register the module path in the registry
3. Return the chunk name string

Instead, it only processes the module path when the route is NOT a module, which means actual modules are being skipped and non-modules are being incorrectly processed.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have broken route chunk generation completely. Routes that should have chunk names registered are now missing from the registry.

---
Repository: /testbed
