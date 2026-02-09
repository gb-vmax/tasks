# Bug Report

### Describe the bug

When using color props with theme colors, the CSS variable syntax is not being applied correctly. Instead of getting the expected `var(--mantine-color-*)` format, the colors are being rendered with incorrect variable references.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function Demo() {
  return (
    <Box bg="blue.5">
      Content
    </Box>
  );
}
```

When inspecting the rendered element, the background color is not being applied correctly. The CSS variable format appears to be malformed.

### Expected behavior

The component should render with the proper CSS variable syntax like `var(--mantine-color-blue-5)` so that the theme color is applied correctly.

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
