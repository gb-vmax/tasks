# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with module exports in the MDX remark plugin. Properties that should be exported from modules are not being properly enumerated, causing undefined references when trying to access exported functions or objects.

### Reproduction

When using the remark-mdx plugin, attempting to access exported members results in errors:

```js
import { someExportedFunction } from 'remark-mdx';

// Error: someExportedFunction is undefined
someExportedFunction();
```

The issue appears to affect all exports from the module. It seems like the export mechanism is trying to iterate over something incorrectly, possibly treating an array of keys as an object instead of iterating over the actual object properties.

### Expected behavior

All exported functions and objects should be accessible after importing from the module. The exports should work as they did in previous versions.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
