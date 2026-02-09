# Bug Report

### Describe the bug
The `all()` function in the plugin-data model is not returning the correct data. When trying to retrieve all plugin data for a specific plugin, the function returns incorrect or empty results.

### Reproduction
```js
import * as pluginData from './models/plugin-data';

// Store some data for a plugin
await pluginData.setItem('my-plugin', 'key1', 'value1');
await pluginData.setItem('my-plugin', 'key2', 'value2');

// Try to retrieve all data for the plugin
const allData = await pluginData.all('my-plugin');

// Expected: Returns array with both stored items
// Actual: Returns empty array or incorrect results
console.log(allData); // []
```

### Expected behavior
The `all()` function should return all stored data entries for the specified plugin name. If multiple key-value pairs have been stored for a plugin, they should all be returned in the result array.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
