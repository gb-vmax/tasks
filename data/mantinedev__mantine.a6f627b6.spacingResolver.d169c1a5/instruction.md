# Bug Report

### Describe the bug

When using negative spacing values (e.g., `-xs`, `-sm`, `-md`) with Box component style props, the CSS variables are not being resolved correctly. The negative sign is being stripped from the variable name lookup, causing the spacing to not work as expected.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function Demo() {
  return (
    <Box mt="-md">
      This box should have negative top margin
    </Box>
  );
}
```

When inspecting the computed styles, the CSS variable reference is incorrect. Instead of looking up the spacing value for `-md` in the theme, it's looking up `md` (without the negative sign) and then trying to apply the negation.

### Expected behavior

Negative spacing values should properly resolve to their corresponding theme spacing values and apply the negative multiplier. The component should correctly apply negative margins/paddings when using values like `-xs`, `-sm`, `-md`, etc.

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
