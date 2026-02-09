# Bug Report

### Describe the bug

I'm experiencing an issue with the color resolver where the `bright` color token is resolving to the wrong CSS variable. When I try to use `c="bright"` on a component, it's applying `--mantine-color-dimmed` instead of `--mantine-color-bright`.

### Reproduction

```tsx
import { Box } from '@mantine/core';

function MyComponent() {
  return (
    <Box c="bright">
      This text should use the bright color
    </Box>
  );
}
```

When inspecting the element in DevTools, the computed style shows `var(--mantine-color-dimmed)` instead of `var(--mantine-color-bright)`.

### Expected behavior

When using `c="bright"`, the component should apply `var(--mantine-color-bright)` CSS variable, not the dimmed variant.

### System Info

- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
