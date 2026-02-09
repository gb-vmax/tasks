# Bug Report

### Describe the bug

When using `MantineProvider` with custom CSS variables for dark and light color schemes, the dark mode styles are not being applied correctly. The color scheme selector is always generating `data-mantine-color-scheme="light"` regardless of which scheme is being targeted.

### Reproduction

```jsx
import { MantineProvider } from '@mantine/core';

const theme = {
  cssVariablesResolver: () => ({
    variables: {},
    light: {
      '--custom-bg': '#ffffff',
    },
    dark: {
      '--custom-bg': '#000000',
    },
  }),
};

function App() {
  return (
    <MantineProvider theme={theme}>
      {/* Dark mode styles are not applied */}
      <div style={{ background: 'var(--custom-bg)' }}>Content</div>
    </MantineProvider>
  );
}
```

### Expected behavior

When dark mode is active, the selector should be `[data-mantine-color-scheme="dark"]` and dark mode CSS variables should be applied. Currently, both light and dark selectors are being set to `"light"`, so dark mode styles never get applied.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
