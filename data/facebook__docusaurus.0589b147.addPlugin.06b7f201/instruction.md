# Bug Report

### Describe the bug

I'm experiencing an issue with the remark plugin system where plugins aren't being registered correctly. When I try to use the same plugin multiple times with different configurations, it seems like the plugin registration is skipping entries or not merging configurations as expected.

### Reproduction

```js
const processor = unified()
  .use(somePlugin, { option1: 'value1' })
  .use(anotherPlugin)
  .use(somePlugin, { option2: 'value2' })

// The second use of somePlugin doesn't seem to properly update the configuration
// Expected the options to be merged, but getting unexpected behavior
```

### Expected behavior

When registering a plugin that's already been added, the system should:
1. Find the existing plugin entry correctly
2. Merge the new configuration with the existing one (for plain objects)
3. Update the plugin parameters appropriately

Instead, it appears that plugin lookup or configuration merging isn't working properly, leading to either duplicate plugins or missing configuration updates.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
