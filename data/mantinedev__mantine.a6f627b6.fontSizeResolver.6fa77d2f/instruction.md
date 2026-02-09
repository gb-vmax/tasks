# Bug Report

### Describe the bug

Font size values are not being resolved correctly when using string values like 'xs', 'sm', 'md', 'lg', 'xl' or heading values like 'h1', 'h2', etc. The CSS variables are not being applied and the font sizes remain unchanged.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function Demo() {
  return (
    <>
      {/* These font sizes are not working */}
      <Box fz="xs">Extra small text</Box>
      <Box fz="sm">Small text</Box>
      <Box fz="md">Medium text</Box>
      <Box fz="lg">Large text</Box>
      <Box fz="xl">Extra large text</Box>
      
      {/* Heading font sizes also not working */}
      <Box fz="h1">Heading 1 size</Box>
      <Box fz="h2">Heading 2 size</Box>
      <Box fz="h3">Heading 3 size</Box>
    </>
  );
}
```

### Expected behavior

When passing theme font size keys (like 'xs', 'sm', 'md', 'lg', 'xl') or heading identifiers (like 'h1', 'h2', 'h3') to the `fz` prop, the component should apply the corresponding CSS variable and render with the correct font size from the theme.

All text elements should display with their respective sizes, but currently they all appear with the default font size.

### System Info

- @mantine/core version: latest
- Browser: Chrome/Firefox/Safari (affects all browsers)

---
Repository: /testbed
