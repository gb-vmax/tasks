# Bug Report

### Describe the bug

CSS variables ordering issue causing specificity problems with color scheme selectors. When using MantineProvider with custom CSS variables, the shared variables are being applied after the color scheme-specific variables, which breaks the intended cascade order.

### Reproduction

```tsx
import { MantineProvider } from '@mantine/core';

const theme = {
  cssVariablesResolver: () => ({
    variables: {
      '--my-color': 'blue',
    },
    light: {
      '--my-color': 'lightblue',
    },
    dark: {
      '--my-color': 'darkblue',
    },
  }),
};

// The shared variables end up with higher specificity than they should
<MantineProvider theme={theme}>
  <App />
</MantineProvider>
```

The generated CSS has the wrong order - shared variables come last instead of first, causing them to override the color scheme-specific values when they shouldn't.

### Expected behavior

Shared CSS variables should be defined first, then color scheme-specific variables should override them. The cascade order should be:
1. Shared variables (base)
2. Dark mode variables (when dark scheme is active)
3. Light mode variables (when light scheme is active)

This way the color scheme-specific variables properly override the shared ones.

### System Info
- @mantine/core version: latest
- Browser: All browsers affected

---
Repository: /testbed
