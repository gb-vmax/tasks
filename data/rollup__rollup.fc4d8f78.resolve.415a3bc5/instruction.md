# Bug Report

### Describe the bug

I'm experiencing an issue with the `resolve` function in the plugin context where the `skipSelf` parameter seems to be inverted. When `skipSelf` is set to `true`, the plugin is NOT skipping itself during resolution, and when set to `false`, it IS skipping itself. This is the opposite of what the parameter name suggests.

### Reproduction

```js
// In a plugin's resolveId hook
this.resolve(source, importer, { skipSelf: true });
// Expected: Should skip the current plugin during resolution
// Actual: The current plugin is included in the resolution chain

this.resolve(source, importer, { skipSelf: false });
// Expected: Should include the current plugin during resolution  
// Actual: The current plugin is skipped
```

### Expected behavior

When `skipSelf: true` is passed, the current plugin should be skipped during module resolution. When `skipSelf: false`, the current plugin should be included in the resolution chain.

### System Info

- Rollup version: latest
- Node version: 18.x

This is causing circular resolution issues in my plugin where I need to delegate to other plugins but the behavior is backwards from what I expect based on the parameter name.

---
Repository: /testbed
