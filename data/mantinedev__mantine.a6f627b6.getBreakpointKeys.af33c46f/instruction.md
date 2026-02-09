# Bug Report

### Describe the bug

When using responsive style props with breakpoint objects in Mantine components, the styles are not being applied correctly. It seems like breakpoint-specific values are being ignored and only the base value (if provided) is used.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function Demo() {
  return (
    <Box
      p={{
        base: 'xs',
        sm: 'md',
        lg: 'xl'
      }}
    >
      Content
    </Box>
  );
}
```

In this example, the padding should change at different breakpoints (`sm` and `lg`), but it appears that only the `base` value is being applied regardless of screen size.

### Expected behavior

The component should apply different padding values at different breakpoints:
- `xs` padding at base/mobile sizes
- `md` padding at `sm` breakpoint and above
- `xl` padding at `lg` breakpoint and above

### System Info
- @mantine/core version: latest
- Browser: Chrome 120
- OS: macOS

---
Repository: /testbed
