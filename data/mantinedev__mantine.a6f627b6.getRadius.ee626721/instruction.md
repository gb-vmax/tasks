# Bug Report

### Describe the bug

The `getRadius` function is not handling `undefined` values correctly. When passing `undefined` as the radius size, it doesn't return the default radius variable and instead tries to process it through `getSize`, which leads to unexpected behavior.

### Reproduction

```js
import { getRadius } from '@mantine/core';

// This should return the default radius but doesn't work as expected
const radius1 = getRadius(undefined);
console.log(radius1); // Expected: 'var(--mantine-radius-default)'

// Only null returns the default now
const radius2 = getRadius(null);
console.log(radius2); // Returns: 'var(--mantine-radius-default)'
```

### Expected behavior

When `undefined` is passed to `getRadius()`, it should return `'var(--mantine-radius-default)'` just like it did before. This is important for components that have optional radius props where `undefined` is a common default value.

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
