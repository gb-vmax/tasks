# Bug Report

### Describe the bug

After a recent update, environment objects are being modified unexpectedly when loaded. Specifically, properties like `color` and `dataPropertyOrder` are being changed even when they shouldn't be touched.

### Reproduction

```js
const env = {
  _id: 'env_1',
  name: 'My Environment',
  data: {
    apiKey: 'test123',
    baseUrl: 'https://api.example.com'
  },
  color: '#FF5733',
  dataPropertyOrder: null
};

// After loading this environment, the object gets modified:
// - color becomes '#ff5733' (lowercased)
// - dataPropertyOrder is now populated with { apiKey: 0, baseUrl: 1 }
```

This is causing issues when:
1. Comparing environments for changes (they appear modified even when they haven't been edited)
2. Colors with uppercase hex values get normalized to lowercase
3. Environments without explicit property ordering get one added automatically

### Expected behavior

Environment objects should remain unchanged when loaded unless explicitly modified by the user. The migration logic should only run when actually needed for backwards compatibility, not on every environment load.

### Additional context

This seems to affect all environments, whether they're newly created or existing ones. The automatic modifications make it difficult to track actual user changes vs. system modifications.

---
Repository: /testbed
