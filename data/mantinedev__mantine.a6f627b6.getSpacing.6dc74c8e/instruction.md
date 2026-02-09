# Bug Report

### Describe the bug

The `getSpacing` utility function is returning incorrect values. When I pass spacing values like `'xs'`, `'sm'`, `'md'`, etc., the function doesn't return the expected spacing size. Instead, it seems to be producing malformed or unexpected output.

### Reproduction

```js
import { getSpacing } from '@mantine/core';

// This should return the correct spacing value for 'md'
const spacing = getSpacing('md');
console.log(spacing); // Returns unexpected value

// Same issue with other spacing sizes
const smallSpacing = getSpacing('sm');
console.log(smallSpacing); // Also incorrect
```

### Expected behavior

The `getSpacing` function should return the correct CSS value for the given spacing size (e.g., `'xs'`, `'sm'`, `'md'`, `'lg'`, `'xl'`). For example, `getSpacing('md')` should return the medium spacing value defined in the theme.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
