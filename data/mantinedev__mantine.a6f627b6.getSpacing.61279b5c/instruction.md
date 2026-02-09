# Bug Report

### Describe the bug

The `getSpacing` utility function is not working correctly with spacing values. When I try to use spacing tokens in my components, they're not being resolved properly and I'm getting unexpected CSS variable names.

### Reproduction

```tsx
import { getSpacing } from '@mantine/core';

// Expected to get spacing variable like 'var(--mantine-spacing-md)'
const spacing = getSpacing('md');

// But getting something like 'var(--mantine-size-NaN)' instead
console.log(spacing);
```

When using spacing props in components:

```tsx
<Box p="md">
  {/* Padding is not applied correctly */}
</Box>
```

### Expected behavior

The `getSpacing` function should return the correct CSS variable reference for spacing values (e.g., `var(--mantine-spacing-md)` for `'md'`), not convert them to size variables or attempt to parse them as floats.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
