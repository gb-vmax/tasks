# Bug Report

### Describe the bug

When using spacing props with string values (like `xs`, `sm`, `md`, etc.), the spacing is not being applied correctly. Instead of using the theme spacing values, it appears to be converting the string directly to rem units.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function Demo() {
  return (
    <Box p="md" m="lg">
      Content
    </Box>
  );
}
```

The padding and margin should use the theme's spacing scale (`--mantine-spacing-md` and `--mantine-spacing-lg` CSS variables), but instead they're being converted to rem values as if they were numeric strings.

### Expected behavior

When passing theme spacing tokens like `"xs"`, `"sm"`, `"md"`, `"lg"`, `"xl"` to spacing props (padding, margin, etc.), they should resolve to the corresponding CSS variables from the theme (`var(--mantine-spacing-md)`, `var(--mantine-spacing-lg)`, etc.).

This was working correctly before and suddenly stopped working after a recent update.

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
