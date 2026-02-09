# Bug Report

### Describe the bug

I'm experiencing an issue with syntax extensions where multiple extensions are not being properly merged. When I try to register multiple syntax extensions for the same hook, only the last one is applied and previous extensions are lost.

### Reproduction

```js
const processor = remark()
  .use(pluginA) // Adds a syntax extension for a specific hook
  .use(pluginB) // Adds another syntax extension for the same hook

// Only pluginB's extension is active, pluginA's extension is gone
```

When two or more plugins try to extend the same syntax hook, the second plugin completely overwrites the first one instead of merging them together. This breaks compatibility when using multiple markdown plugins that extend the same syntax features.

### Expected behavior

All registered syntax extensions should be merged and work together. If multiple plugins add extensions for the same hook, they should all be active simultaneously rather than overwriting each other.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
