# Bug Report

### Describe the bug

I'm experiencing an issue with the `lh` (line-height) style prop on Box components. When I try to use predefined line-height values from the theme or heading values, they're not being applied correctly. Instead, the component seems to be outputting CSS variables for values that shouldn't match.

### Reproduction

```jsx
import { Box } from '@mantine/core';

// This should use the theme's line-height value but doesn't work
<Box lh="md">
  Text with medium line height
</Box>

// This should use the h1 line-height but also doesn't work
<Box lh="h1">
  Text with h1 line height
</Box>
```

When I inspect the rendered elements, the CSS variables are being applied to values that don't exist in the theme, while valid theme values are being ignored and rendered as literal strings.

### Expected behavior

- When passing a valid theme line-height key (like `"xs"`, `"sm"`, `"md"`, `"lg"`, `"xl"`), it should resolve to the corresponding CSS variable
- When passing a heading value (like `"h1"`, `"h2"`, etc.), it should resolve to the heading's line-height CSS variable
- Invalid values should be passed through as-is

### System Info

- @mantine/core version: 7.x
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
