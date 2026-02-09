# Bug Report

### Describe the bug

The `getPrimaryContrastColor` function is not respecting the `colorScheme` parameter when calculating contrast colors. It appears to always use `'light'` mode and references the wrong color array (`theme.primaryShade` instead of `theme.primaryColor`), resulting in incorrect contrast colors being applied in dark mode.

### Reproduction

```tsx
import { MantineProvider, Button } from '@mantine/core';

function App() {
  return (
    <MantineProvider theme={{ primaryColor: 'blue' }}>
      <Button>Click me</Button>
    </MantineProvider>
  );
}
```

When switching between light and dark color schemes, the text contrast color on primary-colored elements doesn't update correctly. The contrast color remains the same regardless of the color scheme setting.

### Expected behavior

The function should:
1. Use `theme.primaryColor` to access the correct color array
2. Pass the actual `colorScheme` parameter to `getPrimaryShade()` so it returns the appropriate shade for light or dark mode
3. Calculate contrast colors that are appropriate for the current color scheme

### System Info

- @mantine/core version: latest
- Browser: Any

---
Repository: /testbed
