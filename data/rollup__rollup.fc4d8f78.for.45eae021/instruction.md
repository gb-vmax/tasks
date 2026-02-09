# Bug Report

### Describe the bug

When using plugins with the `hookFirst` mechanism, all plugins are being skipped instead of running. It seems like the skipping logic is inverted - plugins that should run are being skipped, and plugins that should be skipped are being executed.

### Reproduction

```js
// Set up multiple plugins
const plugins = [
  {
    name: 'plugin-a',
    resolveId(id) {
      return { id: 'resolved-by-a' };
    }
  },
  {
    name: 'plugin-b',
    resolveId(id) {
      return { id: 'resolved-by-b' };
    }
  }
];

// When calling hookFirst with no skipped plugins
// Expected: First plugin should run and return result
// Actual: No plugins run, returns null
```

### Expected behavior

The `hookFirst` method should iterate through plugins and return the first non-null result. If a plugin is in the `skipped` set, it should be skipped. Otherwise, it should run normally.

Currently, it appears that the skip check is backwards - plugins are only running if they ARE in the skipped set, rather than if they are NOT in the skipped set.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
