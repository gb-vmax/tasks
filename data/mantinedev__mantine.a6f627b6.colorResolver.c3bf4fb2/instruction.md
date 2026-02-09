# Bug Report

### Describe the bug

The color resolver is not handling the 'dimmed' color correctly. When I try to use `c="dimmed"` on a component, it doesn't apply the dimmed color variable. Instead, it seems to be returning the wrong CSS variable or value.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function Demo() {
  return (
    <Box c="dimmed">
      This text should be dimmed
    </Box>
  );
}
```

### Expected behavior

When using `c="dimmed"`, the component should apply `var(--mantine-color-dimmed)` as the color value. The text should render with the dimmed color from the theme.

### Actual behavior

The dimmed color is not being applied correctly. It looks like regular colors are being returned instead of the dimmed CSS variable.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
