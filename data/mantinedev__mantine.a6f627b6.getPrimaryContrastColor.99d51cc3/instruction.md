# Bug Report

### Describe the bug

The `getPrimaryContrastColor` function is not respecting the `autoContrast` theme setting. When I set `autoContrast` in my theme configuration, the primary color contrast is not being calculated correctly and always falls back to default behavior instead of using my theme's `autoContrast` value.

### Reproduction

```tsx
import { MantineProvider, createTheme } from '@mantine/core';

const theme = createTheme({
  primaryColor: 'blue',
  autoContrast: true,
});

function App() {
  return (
    <MantineProvider theme={theme}>
      {/* Primary color contrast is not calculated using autoContrast setting */}
      <Button>Click me</Button>
    </MantineProvider>
  );
}
```

### Expected behavior

When `autoContrast` is set in the theme, the `getPrimaryContrastColor` function should use that value to determine the contrast color for the primary color. Currently it seems to ignore the theme's `autoContrast` configuration.

### System Info

- @mantine/core version: latest
- Browser: Chrome 120
- OS: macOS

---
Repository: /testbed
