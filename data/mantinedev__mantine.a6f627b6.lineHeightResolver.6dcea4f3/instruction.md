# Bug Report

### Describe the bug

The `lineHeight` style prop is not working correctly when passing theme line height values. When I try to use predefined line height values from the theme (like 'xs', 'sm', 'md', 'lg', 'xl'), they are not being resolved to the correct CSS variables.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function Demo() {
  return (
    <>
      <Box lh="md">This should use theme line height md</Box>
      <Box lh="lg">This should use theme line height lg</Box>
      <Box lh="h1">This should use h1 line height</Box>
    </>
  );
}
```

### Expected behavior

When using `lh="md"` or other theme line height keys, it should resolve to the appropriate CSS variable like `var(--mantine-line-height-md)`. Similarly, when using heading values like `lh="h1"`, it should resolve to `var(--mantine-h1-line-height)`.

Currently, the line heights are not being applied correctly and the text appears with default browser line heights instead of the theme values.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
