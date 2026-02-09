# Bug Report

### Describe the bug

When using the remark processor with plugins, I'm encountering unexpected behavior where plugin configurations are not being properly updated when the same plugin is registered multiple times with different options.

### Reproduction

```js
const processor = unified()
  .use(somePlugin, { option: 'initial' })
  .use(somePlugin, { option: 'updated' });

// Expected: plugin should be configured with { option: 'updated' }
// Actual: plugin configuration is not updated as expected
```

### Steps to reproduce:
1. Create a unified processor instance
2. Register a plugin with initial options
3. Register the same plugin again with updated options
4. The plugin doesn't receive the updated configuration

### Expected behavior

When a plugin is registered multiple times, the options should be merged or replaced properly. The second call should update the plugin's configuration.

### Additional context

This seems to affect how plugins are tracked and updated in the processor. The issue appears when trying to reconfigure an existing plugin rather than adding a new one.

---
Repository: /testbed
