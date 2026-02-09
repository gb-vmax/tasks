# Bug Report

### Describe the bug
The `all()` function in the plugin-data model is returning incorrect data. When trying to retrieve all plugin data for a specific plugin, the function returns the plugin name string instead of the actual data array from the database.

### Reproduction
```js
import * as pluginData from './models/plugin-data';

// Store some data for a plugin
await pluginData.setByKey('my-plugin', 'setting1', { value: 'test' });
await pluginData.setByKey('my-plugin', 'setting2', { value: 'test2' });

// Try to retrieve all data for the plugin
const result = await pluginData.all('my-plugin');

console.log(result);
// Expected: Array of PluginData objects
// Actual: 'my-plugin' (just the string)
```

### Expected behavior
The `all()` function should return an array of PluginData objects matching the specified plugin, not the plugin name itself.

### System Info
- Insomnia version: latest
- OS: macOS

This is breaking plugin storage functionality as we can't retrieve stored plugin data anymore.

---
Repository: /testbed
