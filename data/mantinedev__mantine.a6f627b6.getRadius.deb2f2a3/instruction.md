# Bug Report

### Describe the bug

I'm experiencing an issue with the `getRadius` utility function. When I pass a radius value, it seems to be ignored and the default radius is always applied instead. Additionally, when a custom radius value is provided, it appears to be referencing the wrong CSS variable.

### Reproduction

```js
import { getRadius } from '@mantine/core';

// This returns the default radius even though I'm passing a specific value
const radius1 = getRadius('sm');
console.log(radius1); // Expected: var(--mantine-radius-sm), but gets default

// When undefined is passed, it doesn't return the default
const radius2 = getRadius(undefined);
console.log(radius2); // Expected: var(--mantine-radius-default)
```

### Expected behavior

- When a radius value (like 'sm', 'md', 'lg') is passed, it should return the corresponding CSS variable (e.g., `var(--mantine-radius-sm)`)
- When `undefined` is passed, it should return `var(--mantine-radius-default)`
- The function should reference the correct `mantine-radius` CSS variables, not other variable types

### System Info

- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
