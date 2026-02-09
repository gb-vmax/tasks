# Bug Report

### Describe the bug

When using color props with Mantine components, colors that should resolve to CSS variables are not being applied correctly. Instead of getting the actual color value, the component seems to be using the variable name itself without the `var()` wrapper.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function Demo() {
  return (
    <Box bg="blue.5">
      This box should have a blue background
    </Box>
  );
}
```

### Expected behavior

The Box component should render with the correct background color from the theme. The color should be resolved to `var(--mantine-color-blue-5)` and applied properly.

### Actual behavior

The background color is not applied correctly. When inspecting the element, it appears the CSS variable is not being properly wrapped with `var()`, causing the color to not resolve.

### System Info

- @mantine/core version: 7.x
- Browser: Chrome 120
- React version: 18.x

This seems to have started happening recently. Colors passed as strings work fine, but theme colors referenced through the color resolver are broken.

---
Repository: /testbed
