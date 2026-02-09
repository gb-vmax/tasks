# Bug Report

### Describe the bug

When using MantineProvider with custom CSS variables for dark mode, the dark mode styles are being applied to light mode instead. It seems like the dark and light color schemes are being swapped somehow.

### Reproduction

```tsx
import { MantineProvider } from '@mantine/core';

function App() {
  return (
    <MantineProvider
      theme={{
        cssVariablesResolver: () => ({
          variables: {},
          light: {
            '--custom-bg': '#ffffff',
            '--custom-text': '#000000'
          },
          dark: {
            '--custom-bg': '#1a1a1a',
            '--custom-text': '#ffffff'
          }
        })
      }}
    >
      {/* App content */}
    </MantineProvider>
  );
}
```

When switching to dark mode, the light mode CSS variables are applied instead, and vice versa. The background and text colors appear inverted from what they should be.

### Expected behavior

Dark mode CSS variables should be applied when the color scheme is set to dark, and light mode variables should be applied when the color scheme is set to light.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
