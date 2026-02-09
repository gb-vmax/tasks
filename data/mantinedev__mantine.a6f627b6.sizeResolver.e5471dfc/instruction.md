# Bug Report

### Describe the bug

I'm experiencing an issue with size values in Mantine components. When I pass numeric values (like `width={100}` or `height={200}`), they're being converted to rem units instead of being treated as pixel values. This is causing unexpected sizing behavior.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function MyComponent() {
  return (
    <Box width={100} height={200}>
      Content
    </Box>
  );
}
```

When passing numeric values directly, the component is applying `rem()` conversion to them, which results in incorrect sizes. For example, `width={100}` gets converted to rem instead of being treated as `100px`.

### Expected behavior

Numeric values should be converted to rem units (e.g., `100` → `6.25rem` with default font size). String values like `"100px"` or `"50%"` should be passed through as-is.

Currently it seems like the behavior is inverted - numbers are not being converted when they should be.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
