# Bug Report

### Describe the bug

When using responsive style props with the `base` property, the function returns a boolean `true` instead of the actual base value. This breaks styling when trying to use responsive values with a base configuration.

### Reproduction

```js
import { getBaseValue } from '@mantine/core';

const styleValue = {
  base: 'md',
  sm: 'lg',
  md: 'xl'
};

const result = getBaseValue(styleValue);
console.log(result); // Expected: 'md', Actual: true
```

### Expected behavior

The `getBaseValue` function should return the actual value of the `base` property (e.g., `'md'`), not a boolean indicating whether the property exists.

### System Info
- @mantine/core version: latest
- Framework: React

---
Repository: /testbed
