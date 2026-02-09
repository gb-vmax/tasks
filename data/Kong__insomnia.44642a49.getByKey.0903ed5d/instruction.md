# Bug Report

### Describe the bug

After a recent update, plugin data retrieval seems to be returning stale/cached values instead of the latest data from the database. When I update plugin data using the API and then immediately retrieve it, I'm getting the old value back instead of the updated one.

### Reproduction

```js
// Set initial value
await pluginData.setByKey('my-plugin', 'config', 'initial-value');

// Get the value - works fine
let data = await pluginData.getByKey('my-plugin', 'config');
console.log(data.value); // 'initial-value'

// Update the value directly in the database or through another process
await pluginData.setByKey('my-plugin', 'config', 'updated-value');

// Try to get the updated value
data = await pluginData.getByKey('my-plugin', 'config');
console.log(data.value); // Still shows 'initial-value' instead of 'updated-value'
```

### Expected behavior

When plugin data is updated, subsequent calls to `getByKey()` should return the most recent value from the database, not a cached version.

### Additional context

This is causing issues in my plugin where configuration changes aren't being picked up immediately. I have to restart the application for the new values to be recognized.

Is there some kind of caching layer that was introduced? If so, how do we invalidate it when data changes?

---
Repository: /testbed
