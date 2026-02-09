# Bug Report

### Describe the bug

Plugin data creation is broken - plugins can't store their data anymore. When trying to create plugin data, the `type` field is being set to `undefined` instead of the correct type value, which causes the data to not be properly stored or retrieved.

### Reproduction

```js
import * as pluginData from './models/plugin-data';

// Try to create plugin data for a plugin
const data = pluginData.create({
  pluginId: 'my-plugin',
  key: 'settings',
  value: { theme: 'dark' }
});

// The created data object has type: undefined
// This breaks plugin data storage
console.log(data.type); // undefined instead of expected type
```

### Expected behavior

The `create` function should properly set the `type` field to the correct model type (like other model creation functions do), not override it with `undefined`. Plugin data should be created with all required fields including the type.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
