# Bug Report

### Describe the bug

CSS variables for component sizes are not being generated correctly. It looks like the variable names have the wrong format and the first size value is being skipped entirely.

### Reproduction

```tsx
import { MantineProvider } from '@mantine/core';

const theme = {
  spacing: {
    xs: '10px',
    sm: '12px',
    md: '16px',
    lg: '20px',
    xl: '24px'
  }
};

// When using MantineProvider with custom spacing
<MantineProvider theme={theme}>
  {/* Components here */}
</MantineProvider>
```

When inspecting the generated CSS variables in the browser, I'm seeing:
- The `xs` size is completely missing from the CSS variables
- The variable names are in the wrong order (e.g., `--mantine-sm-spacing` instead of `--mantine-spacing-sm`)

This means components that rely on these CSS variables don't have access to the smallest size value, and any custom CSS that references the variables using the expected naming convention won't work.

### Expected behavior

All size values (including `xs`) should be present as CSS variables with the correct naming format: `--mantine-{property}-{size}` (e.g., `--mantine-spacing-xs`, `--mantine-spacing-sm`, etc.)

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
