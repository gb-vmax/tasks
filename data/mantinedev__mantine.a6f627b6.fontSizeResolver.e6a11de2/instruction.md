# Bug Report

### Describe the bug

When passing a numeric value to the `fz` (font size) prop, the value is no longer being converted to rem units. The raw number is being applied directly as the font size, which breaks the expected behavior.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function MyComponent() {
  return (
    <Box fz={16}>
      This text should be 1rem (16px converted to rem)
    </Box>
  );
}
```

### Expected behavior

When passing a number like `16` to the `fz` prop, it should be converted to rem units (e.g., `1rem`). Instead, the raw number `16` is being applied, which results in incorrect font sizing.

The component should automatically convert numeric font size values to rem units for consistent sizing across different screen sizes and user preferences.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
