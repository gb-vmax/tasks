# Bug Report

### Describe the bug

The `skipSelf` option in the `resolve` hook is behaving incorrectly - it's now skipping resolution when `skipSelf` is `true` instead of when it's `false`. This causes module resolution to fail in scenarios where a plugin needs to prevent infinite loops by skipping itself.

### Reproduction

```js
// In a plugin's resolveId hook
this.resolve(source, importer, {
  skipSelf: true  // Should skip this plugin, but doesn't work correctly
})
```

When `skipSelf` is set to `true`, the resolution should exclude the current plugin from the resolution chain. However, it appears to be doing the opposite - passing `null` instead of the skip array when `skipSelf` is truthy.

### Expected behavior

When `skipSelf: true` is passed to `resolve()`, the current plugin should be excluded from the resolution process to prevent infinite recursion. When `skipSelf: false` or not provided, the plugin should be included in the resolution chain.

### Additional context

This seems to have broken plugin resolution logic where plugins need to delegate to other plugins or the default resolver without creating circular dependencies.

---
Repository: /testbed
