# Bug Report

### Describe the bug

The `getRadius` utility function is not working correctly. When I pass `undefined` as the radius value, it's not returning the default radius CSS variable. Also, when I provide a specific radius size, it seems to be using the wrong CSS variable prefix.

### Reproduction

```js
import { getRadius } from '@mantine/core';

// This should return 'var(--mantine-radius-default)' but doesn't
const defaultRadius = getRadius(undefined);
console.log(defaultRadius); // Not getting the expected default

// This should use radius variables but seems to use spacing instead
const customRadius = getRadius('md');
console.log(customRadius); // Returns spacing variable instead of radius
```

### Expected behavior

- When `undefined` is passed, it should return `'var(--mantine-radius-default)'`
- When a size value is passed (like `'sm'`, `'md'`, `'lg'`), it should use the `mantine-radius` CSS variable prefix, not `mantine-spacing`

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
