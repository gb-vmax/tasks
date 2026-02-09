# Bug Report

### Describe the bug

The `all()` function in the plugin-data model is not returning the correct plugin data. When trying to retrieve all data for a specific plugin, it returns an empty array or incorrect results even when data exists for that plugin.

### Reproduction

```js
import * as pluginData from './models/plugin-data';

// Store some data for a plugin
await pluginData.setItem('my-plugin', 'key1', 'value1');
await pluginData.setItem('my-plugin', 'key2', 'value2');

// Try to retrieve all data for the plugin
const allData = await pluginData.all('my-plugin');

// Expected: Returns array with 2 items
// Actual: Returns empty array or incorrect results
console.log(allData); // []
```

### Expected behavior

The `all()` function should return all stored data entries for the specified plugin. If I've stored multiple key-value pairs for a plugin, calling `all('my-plugin')` should return an array containing all those entries.

### Additional context

This seems to have broken recently. Other plugin data functions like `setItem()` and `getItem()` work fine, but retrieving all data for a plugin doesn't work anymore.

---
Repository: /testbed
