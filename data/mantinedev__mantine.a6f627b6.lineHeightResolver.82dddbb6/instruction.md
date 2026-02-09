# Bug Report

### Describe the bug

I'm experiencing an issue with the `lineHeight` style prop where passing certain values causes incorrect CSS variable references to be generated. It seems like the validation logic for line height values isn't working as expected.

### Reproduction

```jsx
import { Box } from '@mantine/core';

// This generates an incorrect CSS variable
<Box lh="md">Content</Box>

// Expected: var(--mantine-line-height-md)
// Actual: Generates incorrect variable reference
```

When I pass a standard line height value like `"md"`, `"sm"`, or `"lg"` to the `lh` prop, it doesn't resolve to the correct CSS variable from the theme. The component renders but the line height isn't applied correctly.

### Expected behavior

The `lineHeight` prop should:
1. Check if the value exists in `theme.lineHeights` and generate `var(--mantine-line-height-{value})`
2. Check if the value is a heading (`h1`, `h2`, etc.) and generate `var(--mantine-{value}-line-height)`
3. Otherwise, use the value as-is

Currently it seems to be checking against the wrong theme property or skipping validation entirely.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
