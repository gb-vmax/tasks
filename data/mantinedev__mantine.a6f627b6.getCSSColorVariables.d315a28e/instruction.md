# Bug Report

### Describe the bug

I'm experiencing an issue with color variables in the dark color scheme. When using components with the `filled` variant, the hover state color appears to be incorrect - it's darker than the base color instead of lighter, which makes the hover effect look inverted.

### Reproduction

```tsx
import { Button, MantineProvider } from '@mantine/core';

function Demo() {
  return (
    <MantineProvider theme={{ colorScheme: 'dark' }}>
      <Button variant="filled" color="blue">
        Hover me
      </Button>
    </MantineProvider>
  );
}
```

When hovering over the button in dark mode, the color gets darker instead of lighter. The same issue appears to affect the `light` variant's text color as well.

### Expected behavior

In dark mode, hovering over a filled button should make it slightly lighter/more vibrant, not darker. The hover effect should provide visual feedback that makes the button appear more interactive.

### System Info
- @mantine/core version: latest
- Browser: Firefox/Chrome
- Color scheme: dark

---
Repository: /testbed
