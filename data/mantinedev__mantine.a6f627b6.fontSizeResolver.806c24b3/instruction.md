# Bug Report

### Describe the bug

The `fz` (font-size) prop is not working correctly when passing heading values like `h1`, `h2`, etc. Instead of applying the heading font sizes, it seems to be treating them as regular string values.

Also, when using numeric values for font size, the values are not being converted to rem units as expected.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function Demo() {
  return (
    <>
      {/* This should use the h1 font size but doesn't work */}
      <Box fz="h1">Heading 1 size</Box>
      
      {/* This should use the h2 font size but doesn't work */}
      <Box fz="h2">Heading 2 size</Box>
      
      {/* Numeric values should be converted to rem but aren't */}
      <Box fz={16}>16px text</Box>
    </>
  );
}
```

### Expected behavior

- When passing heading values (`h1`, `h2`, `h3`, etc.) to the `fz` prop, it should apply the corresponding heading font size CSS variable (`var(--mantine-h1-font-size)`, etc.)
- When passing numeric values, they should be automatically converted to rem units using the `rem()` helper

### System Info

- @mantine/core version: 7.x
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
