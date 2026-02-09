# Bug Report

### Describe the bug

When using the `color` prop with the value `"dimmed"` on Mantine components, the color is not being applied correctly. Instead of showing the dimmed color, it appears to be using the bright color variant.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function Demo() {
  return (
    <Box c="dimmed">
      This text should be dimmed but appears bright instead
    </Box>
  );
}
```

### Expected behavior

When `c="dimmed"` is used, the component should apply `var(--mantine-color-dimmed)` and display text in the dimmed color variant. Currently it seems to be resolving to the wrong CSS variable.

### System Info

- @mantine/core version: 7.x
- Browser: Chrome/Firefox

---
Repository: /testbed
