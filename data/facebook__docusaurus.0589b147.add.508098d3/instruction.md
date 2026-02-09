# Bug Report

### Describe the bug

I'm encountering an issue with plugin configuration when passing plugin tuples to the processor. When I try to use a plugin with parameters in array format, the parameters aren't being passed correctly to the plugin.

### Reproduction

```js
const processor = remark();

// Trying to add a plugin with parameters as a tuple
processor.use([myPlugin, { option1: true, option2: 'value' }]);

// The plugin receives incorrect parameters - it seems to be getting 
// the entire array instead of just the options object
```

### Expected behavior

When passing a plugin as a tuple `[plugin, ...parameters]`, the plugin should receive only the parameters portion (everything after the first element), not the entire array including the plugin function itself.

The plugin function should be called with just the options/parameters, similar to:
```js
myPlugin({ option1: true, option2: 'value' })
```

Instead, it appears to be receiving the full tuple array.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
