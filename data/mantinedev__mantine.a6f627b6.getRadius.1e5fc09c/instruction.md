# Bug Report

### Describe the bug

The `getRadius()` utility function is returning incorrect CSS variable values. When I pass a radius size value, it returns the default radius instead of the actual size. Also, even when I don't pass any value (undefined), it still returns a CSS variable but seems to be using the wrong variable name.

### Reproduction

```js
import { getRadius } from '@mantine/core';

// This returns 'var(--mantine-radius-default)' when it should use the provided size
const radius1 = getRadius('md');

// This also returns 'var(--mantine-radius-default)' 
const radius2 = getRadius('lg');

// Even undefined returns 'var(--mantine-radius-default)'
const radius3 = getRadius(undefined);
```

### Expected behavior

- When passing a specific radius size (like 'md', 'lg', etc.), it should return the corresponding CSS variable for that size
- When passing `undefined`, it should return the default radius variable
- The function should use the correct `mantine-radius` CSS variable prefix, not spacing variables

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
