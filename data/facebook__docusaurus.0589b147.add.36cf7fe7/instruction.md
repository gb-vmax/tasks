# Bug Report

### Describe the bug
When using the `use()` method with plugin tuples (array format), the plugin parameters are not being passed correctly. The array check logic appears to be inverted, causing plugin tuples to be treated as presets and non-arrays to be treated as tuples.

### Reproduction
```js
// Using a plugin with parameters as a tuple
processor.use([remarkPlugin, { option1: true, option2: 'value' }])

// The plugin receives the entire array instead of just the parameters
// Expected: plugin gets called with { option1: true, option2: 'value' }
// Actual: plugin gets called with the full array [remarkPlugin, { option1: true, option2: 'value' }]
```

### Expected behavior
When passing a plugin as a tuple `[plugin, ...parameters]`, the plugin should be called with only the parameters portion, not the entire array. Non-array objects should be treated as presets.

### Additional context
This seems to affect the remark processor's plugin system. The issue occurs when trying to configure plugins with options using the tuple syntax, which is a common pattern in the unified/remark ecosystem.

---
Repository: /testbed
