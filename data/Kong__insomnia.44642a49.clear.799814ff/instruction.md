# Bug Report

### Describe the bug
The plugin store's `clear()` method is not working as expected. When I call `store.clear()` to remove all data for a plugin, the operation seems to hang or take an extremely long time to complete. This is blocking my plugin's cleanup functionality.

### Reproduction
```js
// In a plugin
module.exports.requestHooks = [
  context => {
    const { store } = context;
    
    // Set some data
    await store.setItem('key1', 'value1');
    await store.setItem('key2', 'value2');
    
    // Try to clear all data - this hangs
    await store.clear();
  }
];
```

### Expected behavior
The `clear()` method should quickly remove all stored data for the plugin and return without delays.

### Additional context
This issue started appearing recently. The method used to work fine before, but now it seems like there's some additional processing happening that's causing the delay. My plugin needs to clear its data frequently, so this is becoming a major blocker.

---
Repository: /testbed
