# Bug Report

### Describe the bug

I'm experiencing an issue with spacing values in the Box component. When using custom spacing values from the theme (like `xl`, `md`, etc.), they're not being applied correctly. Instead, the raw string value is being used as a rem value.

### Reproduction

```jsx
import { Box, MantineProvider } from '@mantine/core';

const theme = {
  spacing: {
    xs: '0.625rem',
    sm: '0.75rem',
    md: '1rem',
    lg: '1.25rem',
    xl: '1.5rem',
  }
};

function App() {
  return (
    <MantineProvider theme={theme}>
      <Box p="xl" m="lg">
        Content here
      </Box>
    </MantineProvider>
  );
}
```

### Expected behavior

The Box component should use the spacing values defined in the theme (e.g., `xl` should resolve to `var(--mantine-spacing-xl)` or the corresponding theme value). Instead, it seems to be treating theme spacing keys as if they don't exist in the theme and converting them to rem values directly.

This affects all spacing props like `p`, `m`, `px`, `py`, `mx`, `my`, etc. when using theme spacing tokens.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
