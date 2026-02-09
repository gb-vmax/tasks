# Bug Report

### Describe the bug

I'm experiencing an issue with plugin global data where data from different plugin instances is being overwritten instead of being stored separately. When multiple instances of the same plugin are used (with different IDs), only the last instance's data is retained.

### Reproduction

```js
// Configure multiple instances of the same plugin
module.exports = {
  plugins: [
    ['my-plugin', { id: 'instance1' }],
    ['my-plugin', { id: 'instance2' }],
  ],
};

// In the plugin:
contentLoaded({ actions }) {
  actions.setGlobalData({ value: 'data-for-this-instance' });
}

// Expected: Both instances should have their data stored
// Actual: Only the last instance's data is available
```

### Expected behavior

Each plugin instance should maintain its own global data independently. When accessing global data, I should be able to retrieve data for each plugin ID separately without one instance overwriting another's data.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have started recently, possibly after a refactoring of the plugin system. The global data for earlier plugin instances is getting lost when subsequent instances call `setGlobalData`.

---
Repository: /testbed
