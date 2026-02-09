# Bug Report

### Describe the bug

The `store.hasItem()` method in the plugin context is returning incorrect results. When checking if a key exists in the plugin store, it returns `true` even when an error occurs during the lookup, which leads to false positives.

### Reproduction

```js
// In a plugin
const plugin = {
  name: 'my-plugin'
};

const { store } = init(plugin);

// When an error occurs during getByKey (e.g., database connection issue)
// hasItem incorrectly returns true instead of handling the error properly
const exists = await store.hasItem('some-key');
// Expected: false or throw error
// Actual: true
```

### Expected behavior

When checking if an item exists:
- Should return `true` if the item exists
- Should return `false` if the item doesn't exist
- Should not return `true` when an error occurs

The current implementation catches errors and returns `true`, which masks actual problems and causes plugins to behave as if keys exist when they might not.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
