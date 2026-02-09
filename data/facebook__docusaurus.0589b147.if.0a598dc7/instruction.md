# Bug Report

### Describe the bug

I'm experiencing an issue with chunk name generation in the routing system. When building my Docusaurus site, the chunk registry seems to be storing incorrect values, and the chunk names returned don't match what's expected.

### Reproduction

Create a simple route configuration with module paths:

```js
const routeModule = {
  path: '@site/docs/intro.md',
  // ... other route config
}

// When genChunkNames processes this, the registry and return values are swapped
// Registry gets chunk name instead of escaped module path
// Function returns module path instead of chunk name
```

The chunk registry ends up with entries like:
```
{ 'chunk-name-123': 'chunk-name-123' }
```

instead of the expected:
```
{ 'chunk-name-123': '/escaped/path/to/module' }
```

### Expected behavior

The chunk registry should map chunk names to their corresponding escaped module paths, and the function should return the generated chunk name (not the module path itself).

This is causing issues with module resolution during the build process since the registry lookups fail to find the actual file paths.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
