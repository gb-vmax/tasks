# Bug Report

### Describe the bug
When using the `getSpacing` utility function, it's not returning the correct CSS variable references. The function seems to be using the wrong prefix for spacing values, which causes spacing-related styles to not work as expected.

### Reproduction
```js
import { getSpacing } from '@mantine/core';

// This should return 'var(--mantine-spacing-md)'
// but instead returns 'var(--mantine-size-md)'
const spacing = getSpacing('md');
console.log(spacing); // Outputs wrong CSS variable
```

### Expected behavior
The `getSpacing` function should return spacing-specific CSS variables with the `--mantine-spacing-` prefix, not the generic `--mantine-size-` prefix. This is causing components that rely on spacing utilities to use incorrect values.

### System Info
- @mantine/core version: latest
- Framework: React

---
Repository: /testbed
