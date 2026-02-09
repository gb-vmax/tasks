# Bug Report

### Describe the bug

When using the `radius` style prop with numeric values, the output is no longer converted to rem units. This breaks responsive styling and causes layout issues when numeric radius values are passed to components.

### Reproduction

```jsx
import { Box } from '@mantine/core';

// This no longer converts the number to rem units
<Box radius={16}>Content</Box>

// Expected: border-radius should be 1rem (16px converted to rem)
// Actual: border-radius is just 16 (unitless, which is invalid CSS)
```

The issue occurs with any numeric radius value:

```jsx
<Box radius={8}>Content</Box>  // Should be 0.5rem, but renders as 8
<Box radius={24}>Content</Box> // Should be 1.5rem, but renders as 24
```

### Expected behavior

Numeric radius values should be automatically converted to rem units using the `rem()` utility function, just like other numeric spacing/sizing properties in Mantine. This ensures consistent responsive behavior across different screen sizes and user font preferences.

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
