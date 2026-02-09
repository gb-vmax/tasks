# Bug Report

### Describe the bug

The `fontSizeResolver` is not correctly handling heading values (h1-h6). When I pass a heading value like `'h1'` or `'h2'` to a component's `fz` prop, it's not resolving to the correct CSS variable.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function Demo() {
  return (
    <>
      <Box fz="h1">This should use h1 font size</Box>
      <Box fz="h2">This should use h2 font size</Box>
      <Box fz="h3">This should use h3 font size</Box>
    </>
  );
}
```

The heading font sizes are not being applied. Instead, the values seem to be treated as regular strings and converted to rem units.

### Expected behavior

When passing heading values (`'h1'`, `'h2'`, `'h3'`, `'h4'`, `'h5'`, `'h6'`) to the font size prop, it should resolve to the corresponding CSS variable like `var(--mantine-h1-font-size)`, `var(--mantine-h2-font-size)`, etc.

This used to work in previous versions but seems to have broken recently.

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
