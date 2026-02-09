# Bug Report

### Describe the bug

Responsive style props are not working correctly when using breakpoint-specific values. Only the `base` value is being applied, and all breakpoint-specific styles (like `xs`, `sm`, `md`, `lg`, `xl`) are being ignored.

### Reproduction

```tsx
import { Box } from '@mantine/core';

function Demo() {
  return (
    <Box
      p={{
        base: '10px',
        sm: '20px',
        md: '30px',
        lg: '40px'
      }}
    >
      Content
    </Box>
  );
}
```

In this example, the padding should change at different breakpoints, but it stays at `10px` (the base value) regardless of screen size.

### Expected behavior

The component should apply different padding values based on the current viewport width:
- `10px` for mobile (base)
- `20px` at `sm` breakpoint
- `30px` at `md` breakpoint  
- `40px` at `lg` breakpoint

Instead, only the base value is applied and breakpoint-specific values are completely ignored.

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox
- OS: macOS

---
Repository: /testbed
