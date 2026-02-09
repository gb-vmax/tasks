# Bug Report

### Describe the bug
When using the `ff` (font family) style prop with predefined values like `'monospace'`, `'text'`, or `'heading'`, the component is rendering the literal string value instead of resolving it to the actual CSS variable from the theme.

### Reproduction
```jsx
import { Box } from '@mantine/core';

function Demo() {
  return (
    <Box ff="monospace">
      This text should use the monospace font family
    </Box>
  );
}
```

The text is rendered with `font-family: "monospace"` instead of the expected CSS variable `var(--mantine-font-family-monospace)`.

### Expected behavior
The `ff` prop should resolve predefined font family values (`monospace`, `text`, `heading`) to their corresponding CSS variables from the theme:
- `ff="monospace"` should resolve to `var(--mantine-font-family-monospace)`
- `ff="text"` should resolve to `var(--mantine-font-family-text)`
- `ff="heading"` should resolve to `var(--mantine-font-family-heading)`

Custom font family strings should still be passed through as-is.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120
- React version: 18.x

---
Repository: /testbed
