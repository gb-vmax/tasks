# Bug Report

### Describe the bug

I'm experiencing an issue with the `lineHeight` style prop when using heading values like 'h1', 'h2', etc. The generated CSS variable reference appears to be incorrect and doesn't resolve to the expected line height value.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function MyComponent() {
  return (
    <Box lh="h1">
      This text should use the h1 line height
    </Box>
  );
}
```

When inspecting the rendered element, the CSS variable reference doesn't match the expected format. Instead of getting a proper line height value, the element has a malformed CSS variable.

### Expected behavior

The `lh` prop with heading values ('h1', 'h2', 'h3', etc.) should resolve to the correct CSS variable like `var(--mantine-h1-line-height)` and apply the appropriate line height from the theme.

### Additional context

This seems to affect all heading-based line height values. Regular line height values from `theme.lineHeights` appear to work fine, but specifically the heading shortcuts are broken.

---
Repository: /testbed
