# Bug Report

### Describe the bug

I'm experiencing an issue with text color resolution when using theme colors with specific shades. When I try to apply a theme color with a shade number (like `blue.5`), the color variable being generated doesn't match what I expect.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function MyComponent() {
  return (
    <Box c="blue.5">
      This text should use the blue.5 shade
    </Box>
  );
}
```

When inspecting the rendered element, the CSS variable being used doesn't seem to reference the correct color variable format. It looks like colors with explicit shades are not being resolved to the expected CSS variable.

### Expected behavior

When using a theme color with a specific shade (e.g., `blue.5`), it should resolve to the appropriate CSS variable that references that specific shade. Instead, it seems to be using a different variable format that doesn't work correctly.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
