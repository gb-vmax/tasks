# Bug Report

### Describe the bug

When using the `color` prop with the value `'dimmed'` on Mantine components, the color is not being applied correctly. Instead of resolving to the CSS variable `var(--mantine-color-dimmed)`, it's returning the literal string `'dimmed'`, which doesn't apply any styling.

### Reproduction

```tsx
import { Box } from '@mantine/core';

function MyComponent() {
  return (
    <Box color="dimmed">
      This text should be dimmed but appears unstyled
    </Box>
  );
}
```

### Expected behavior

The component should apply the dimmed color using the CSS variable `var(--mantine-color-dimmed)` and the text should appear with the dimmed color from the theme.

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
