# Bug Report

### Describe the bug

I'm experiencing an issue with chunk name generation in the route handling system. When building the site, the chunk registry seems to be populated incorrectly, causing the wrong mapping between module paths and chunk names.

### Reproduction

When creating routes with modules, the chunk name registry gets inverted values. Instead of mapping chunk names to module paths, it appears to be doing the reverse, and the function returns the module path instead of the chunk name.

This affects how modules are loaded and referenced in the generated output.

### Expected behavior

The `genChunkNames` function should:
1. Map chunk names to escaped module paths in the registry
2. Return the generated chunk name (not the module path)

The registry should look like:
```js
{
  "chunkName123": "/escaped/module/path"
}
```

But it seems to be generating something different.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
