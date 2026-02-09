# Bug Report

### Describe the bug

The `deepMerge` utility function is crashing when trying to merge objects that contain `null` values. It seems like the function is not properly checking for null values before attempting to merge, which causes unexpected behavior.

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
    colors: null
  }
};

// This throws an error or produces unexpected results
const result = deepMerge(target, source);
```

### Expected behavior

The function should handle `null` values gracefully and merge them properly without throwing errors. When a source property is `null`, it should either:
- Replace the target property with `null`, or
- Skip merging that property

### System Info
- @mantine/core version: latest
- Node version: 18.x

---
Repository: /testbed
