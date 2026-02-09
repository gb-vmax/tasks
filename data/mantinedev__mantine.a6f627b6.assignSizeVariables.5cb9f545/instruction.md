# Bug Report

### Describe the bug

CSS variables for size-related theme properties are not being generated correctly. When defining custom sizes in the theme (like spacing, radius, etc.), the CSS variables are not being created with the proper naming convention.

### Reproduction

```js
import { MantineProvider, createTheme } from '@mantine/core';

const theme = createTheme({
  spacing: {
    xs: '0.5rem',
    sm: '0.75rem',
    md: '1rem',
    lg: '1.5rem',
    xl: '2rem',
  }
});

// Expected CSS variables to be generated:
// --mantine-spacing-xs: 0.5rem
// --mantine-spacing-sm: 0.75rem
// --mantine-spacing-md: 1rem
// --mantine-spacing-lg: 1.5rem
// --mantine-spacing-xl: 2rem

// But the variables are not being created properly
```

When inspecting the generated CSS variables in the browser's dev tools, the expected `--mantine-spacing-*` variables are either missing or have incorrect names/values.

### Expected behavior

All defined size values should be converted to CSS variables with the correct naming pattern `--mantine-{propertyName}-{sizeName}` and should contain the corresponding size values.

### System Info

- @mantine/core version: latest
- Browser: Chrome 120
- OS: macOS

---
Repository: /testbed
