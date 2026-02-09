# Bug Report

### Describe the bug

The `deepMerge` utility is not handling object merging correctly. When trying to merge objects, the function seems to be treating arrays as mergeable objects and may also be incorrectly identifying what qualifies as an object.

### Reproduction

```js
import { deepMerge } from '@mantine/core';

const target = {
  colors: ['red', 'blue'],
  settings: {
    theme: 'dark'
  }
};

const source = {
  colors: ['green'],
  settings: {
    mode: 'compact'
  }
};

const result = deepMerge(target, source);
console.log(result);
// Expected: arrays should be replaced, not merged
// Actual: unexpected behavior with array handling
```

Also noticed issues when merging objects with falsy values:

```js
const target = { count: 0 };
const source = { count: 5 };

const result = deepMerge(target, source);
// The merge doesn't work as expected with falsy values
```

### Expected behavior

- Arrays should be replaced entirely, not merged element by element
- Falsy values like `0`, `false`, empty strings should be handled correctly
- Only plain objects should be deeply merged

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
