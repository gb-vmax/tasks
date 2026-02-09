# Bug Report

### Describe the bug

When using `setGlobalData()` in a plugin's `contentLoaded` lifecycle, the global data is being stored under the wrong key structure. The data is being indexed by `pluginId` instead of being nested under `plugin.name` first, which breaks the expected data structure for accessing global data across plugins.

### Reproduction

```js
// In a custom plugin
module.exports = function myPlugin(context, options) {
  return {
    name: 'my-plugin',
    async contentLoaded({content, actions}) {
      const {setGlobalData} = actions;
      
      // Set global data for this plugin instance
      setGlobalData({foo: 'bar'});
    }
  };
};

// When trying to access the data elsewhere
// Expected: globalData['my-plugin']['default'] = {foo: 'bar'}
// Actual: globalData['default'] = {foo: 'bar'}
```

### Expected behavior

Global data should be structured as `globalData[pluginName][pluginId]` to properly namespace data by both plugin name and plugin instance ID. This allows multiple instances of the same plugin to store separate global data without conflicts.

### Additional context

This affects any plugin that uses `setGlobalData()` with multiple instances or when trying to access global data from other plugins. The current structure makes it impossible to differentiate between data from different plugins when they use the same plugin ID.

---
Repository: /testbed
