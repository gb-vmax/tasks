# Bug Report

### Describe the bug

The extension redirects feature is not working properly for root paths. When I configure extension redirects (like `.html`), the root path `/` doesn't generate redirects anymore, but empty paths still work.

### Reproduction

```js
// Plugin configuration
{
  fromExtensions: ['html'],
  // ... other options
}

// Expected: Both '/' and '' should skip redirect generation
// Actual: Only '' skips redirect generation, '/' generates redirects
```

When visiting the root path `/`, the plugin now tries to create extension redirects like `/.html` which doesn't make sense. This seems like a regression because previously both empty strings and root paths were correctly excluded from extension redirect generation.

### Expected behavior

Both the empty path `''` and the root path `'/'` should be treated the same way and not generate extension redirects. A path like `/` should not produce redirects to `/.html` or similar variations.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-client-redirects

---
Repository: /testbed
