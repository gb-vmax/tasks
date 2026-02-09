# Bug Report

### Describe the bug

I'm experiencing an issue where the first plugin in a chain is being skipped when running hooks with the "first" strategy. This means that if the first plugin returns a non-null value, it's completely ignored and the system moves on to check subsequent plugins instead.

### Reproduction

```js
// Plugin setup
const plugins = [
  {
    name: 'plugin-1',
    resolveId(id) {
      if (id === 'virtual-module') {
        return { id: 'resolved-by-first-plugin' };
      }
    }
  },
  {
    name: 'plugin-2',
    resolveId(id) {
      return { id: 'resolved-by-second-plugin' };
    }
  }
];

// When resolving 'virtual-module', plugin-1 should handle it
// but it's being skipped and plugin-2 is called instead
```

### Expected behavior

The first plugin in the chain should be checked first, and if it returns a result, that result should be used. Currently it seems like the first plugin is never even called for "first" hooks.

### Additional context

This appears to affect any hook that uses the "first" resolution strategy. The first plugin is consistently being ignored regardless of what it returns.

---
Repository: /testbed
