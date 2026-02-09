# Bug Report

### Describe the bug

I'm experiencing an issue with CSS color variables in MantineProvider. The `--mantine-color-{name}-text` variable seems to be referencing the wrong color value, and the `--mantine-color-{name}-light-color` variable is producing incorrect shade calculations.

### Reproduction

```jsx
import { MantineProvider } from '@mantine/core';

const App = () => (
  <MantineProvider theme={{ primaryColor: 'blue' }}>
    {/* Components using color variables */}
  </MantineProvider>
);
```

When inspecting the computed CSS variables:
1. `--mantine-color-blue-text` is pointing to `--mantine-color-blue-filled` instead of the expected shade
2. `--mantine-color-blue-light-color` calculates to negative shade values in some cases (e.g., when primaryShade is less than 5)

### Expected behavior

- `--mantine-color-{name}-text` should reference the appropriate color shade directly
- `--mantine-color-{name}-light-color` should never produce negative shade values and should be clamped to valid shade range (0-9)

### System Info

- @mantine/core version: latest
- Browser: Chrome/Firefox

This affects any component that relies on these CSS color variables for styling.

---
Repository: /testbed
