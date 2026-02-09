# Bug Report

### Describe the bug

When a plugin calls `this.resolve()` with `skipSelf: true` (or when it defaults to true), the resolution immediately returns `null` instead of properly skipping the current plugin and continuing with the next plugin in the chain. This breaks plugin resolution chains where plugins need to delegate to other plugins.

### Reproduction

```js
// Plugin A
{
  name: 'plugin-a',
  resolveId(source, importer) {
    if (source === './test.js') {
      // Try to resolve using other plugins
      return this.resolve(source, importer, { skipSelf: true });
    }
  }
}

// Plugin B
{
  name: 'plugin-b',
  resolveId(source, importer) {
    if (source === './test.js') {
      return { id: '/resolved/test.js' };
    }
  }
}
```

When plugin A calls `this.resolve()` with `skipSelf: true`, it returns `null` immediately instead of falling through to plugin B. The expected behavior is that plugin B should handle the resolution since plugin A is skipped.

### Expected behavior

When `skipSelf: true` is used, the current plugin should be skipped but resolution should continue with the remaining plugins in the chain. Only return `null` if a recursive call to the same plugin is detected (same plugin, source, and importer).

### Additional context

This seems to affect any workflow where plugins need to delegate resolution to other plugins in the chain. The resolution just stops prematurely instead of continuing through the plugin list.

---
Repository: /testbed
