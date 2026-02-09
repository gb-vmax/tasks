# Bug Report

### Describe the bug

I'm experiencing an issue with the `deepMerge` utility function where it's not merging nested objects correctly anymore. When I try to merge two objects with nested properties, the function seems to treat objects as arrays and doesn't properly merge the nested values.

### Reproduction

```js
import { deepMerge } from '@mantine/core';

const target = {
  theme: {
    colors: {
      primary: 'blue'
    }
  }
};

const source = {
  theme: {
    colors: {
      secondary: 'red'
    }
  }
};

const result = deepMerge(target, source);
console.log(result);
// Expected: { theme: { colors: { primary: 'blue', secondary: 'red' } } }
// Actual: Objects are not being merged properly
```

### Expected behavior

The `deepMerge` function should recursively merge nested objects, combining properties from both the target and source objects. In the example above, the result should contain both `primary` and `secondary` color values.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
