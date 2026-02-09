# Bug Report

### Describe the bug

I'm experiencing an issue with plugin global data storage where the data structure is not being organized correctly. When multiple plugins set global data, the data is being stored at the wrong level in the global data object.

### Reproduction

```js
// Plugin 1 with ID 'default'
actions.setGlobalData({ foo: 'bar' });

// Plugin 2 with ID 'custom'  
actions.setGlobalData({ baz: 'qux' });

// Expected structure:
// globalData = {
//   'plugin-name': {
//     'default': { foo: 'bar' },
//     'custom': { baz: 'qux' }
//   }
// }

// Actual structure seems wrong - data is keyed by pluginId instead of nested under plugin name
```

### Expected behavior

Global data should be organized hierarchically with plugin name as the top level key and plugin ID as the second level key. This allows multiple instances of the same plugin (with different IDs) to store their data separately under the same plugin name.

### System Info

- Docusaurus version: latest
- Node version: 18.x

This is breaking my multi-instance plugin setup where I have the same plugin loaded multiple times with different configurations.

---
Repository: /testbed
