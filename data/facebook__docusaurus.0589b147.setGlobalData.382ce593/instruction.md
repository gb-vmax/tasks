# Bug Report

### Describe the bug

When using `setGlobalData` in a plugin, the data is being stored under the wrong key. Instead of storing the data under the `pluginId`, it's being stored under `plugin.name` again, which causes issues when trying to access plugin data with specific plugin IDs.

### Reproduction

```js
// In a Docusaurus plugin
export default function myPlugin(context, options) {
  return {
    name: 'my-plugin',
    async contentLoaded({content, actions}) {
      const {setGlobalData} = actions;
      
      // Set global data for a specific plugin instance
      setGlobalData({someData: 'test'});
    },
  };
}

// When trying to access the data elsewhere
// Expected: globalData['my-plugin']['default'] = {someData: 'test'}
// Actual: globalData['my-plugin']['my-plugin'] = {someData: 'test'}
```

### Expected behavior

The global data should be stored under `globalData[plugin.name][pluginId]` so that multiple instances of the same plugin can store their data separately using their unique plugin IDs.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is causing problems when we have multiple instances of the same plugin with different IDs, as they all end up overwriting each other's data.

---
Repository: /testbed
