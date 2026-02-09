# Bug Report

### Describe the bug

When using negative spacing values (e.g., `-xs`, `-sm`, `-md`) with Box component style props, the spacing resolver is not correctly looking up theme values. Instead of using the theme's spacing scale, it falls back to treating the value as a raw CSS unit.

### Reproduction

```jsx
import { Box } from '@mantine/core';

// This should use theme.spacing but doesn't work correctly
<Box m="-xs">Content</Box>
<Box p="-sm">Content</Box>
<Box mt="-md">Content</Box>
```

The issue occurs when trying to use negative spacing values from the theme. The spacing resolver should check if the value (including the minus sign) exists in `theme.spacing`, but it appears to be checking the modified value without the minus sign instead.

### Expected behavior

Negative spacing values like `-xs`, `-sm`, `-md` should correctly resolve to their corresponding theme values (e.g., `calc(var(--mantine-spacing-xs) * -1)`). The component should apply negative margins/padding using the theme's spacing scale.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
