# Bug Report

### Describe the bug

The `deepMerge` utility function is not handling object merging correctly. When trying to merge configuration objects, the function appears to be treating non-object values as objects, causing unexpected behavior and potentially corrupting the merged result.

### Reproduction

```js
import { deepMerge } from '@mantine/core';

const target = {
  theme: {
    colors: {
      primary: '#000'
    }
  }
};

const source = {
  theme: {
    colors: {
      secondary: '#fff'
    }
  }
};

const result = deepMerge(target, source);
// Expected: { theme: { colors: { primary: '#000', secondary: '#fff' } } }
// Actual: Unexpected merge behavior
```

### Expected behavior

The `deepMerge` function should properly identify objects and only perform deep merging on actual object types. Non-object values should be handled appropriately without being treated as mergeable objects.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
