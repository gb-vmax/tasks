# Bug Report

### Describe the bug

The `fz` (font-size) prop is not working correctly with theme font size values. When I try to use predefined font sizes from the theme (like `xs`, `sm`, `md`, `lg`, `xl`), they're not being applied to the component.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function Demo() {
  return (
    <>
      <Box fz="xs">This should use theme xs font size</Box>
      <Box fz="sm">This should use theme sm font size</Box>
      <Box fz="md">This should use theme md font size</Box>
    </>
  );
}
```

The text renders but the font sizes from the theme are not being applied. It seems like the CSS variables for theme font sizes (`--mantine-font-size-xs`, `--mantine-font-size-sm`, etc.) are not being generated.

Also noticed that heading values like `h1`, `h2`, etc. used to work but now they don't apply any font size at all.

```jsx
<Box fz="h1">Heading size text</Box>  // No font size applied
```

### Expected behavior

- When using `fz="xs"`, `fz="sm"`, etc., the component should apply the corresponding theme font size
- When using `fz="h1"`, `fz="h2"`, etc., the component should apply the corresponding heading font size

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
