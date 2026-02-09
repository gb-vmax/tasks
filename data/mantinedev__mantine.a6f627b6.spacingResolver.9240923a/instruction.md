# Bug Report

### Describe the bug

I'm experiencing an issue with negative spacing values in Mantine components. When I try to use a negative spacing value like `-xs` or `-md`, the spacing doesn't work correctly and falls back to using `rem()` conversion instead of the CSS variable.

### Reproduction

```tsx
import { Box } from '@mantine/core';

function MyComponent() {
  return (
    <Box mt="-xs">
      {/* Content */}
    </Box>
  );
}
```

When using negative spacing values (e.g., `mt="-xs"`, `p="-md"`), the component doesn't apply the correct CSS variable. Instead of getting `calc(var(--mantine-spacing-xs) * -1)`, it seems to be treating the value as if it's not in the theme and converting it with `rem()`.

### Expected behavior

Negative spacing values should resolve to `calc(var(--mantine-spacing-{value}) * -1)` using the theme's spacing variables, just like positive spacing values resolve to `var(--mantine-spacing-{value})`.

For example:
- `mt="-xs"` should resolve to `calc(var(--mantine-spacing-xs) * -1)`
- `p="-md"` should resolve to `calc(var(--mantine-spacing-md) * -1)`

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
