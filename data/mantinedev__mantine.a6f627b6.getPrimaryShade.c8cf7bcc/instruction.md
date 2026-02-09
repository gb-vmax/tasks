# Bug Report

### Describe the bug

The `getPrimaryShade` function is returning incorrect shade values based on the color scheme. When using `colorScheme: 'light'`, it returns the dark shade instead of the light shade, and vice versa. This causes components to use the wrong primary color shade in light/dark mode.

### Reproduction

```tsx
import { MantineProvider, useMantineTheme } from '@mantine/core';

function App() {
  return (
    <MantineProvider
      theme={{
        primaryShade: { light: 6, dark: 8 }
      }}
    >
      <TestComponent />
    </MantineProvider>
  );
}

function TestComponent() {
  const theme = useMantineTheme();
  
  // With colorScheme='light', this returns 8 (dark shade) instead of 6 (light shade)
  const shade = getPrimaryShade(theme, 'light');
  console.log('Light mode shade:', shade); // Expected: 6, Actual: 8
  
  // With colorScheme='dark', this returns 6 (light shade) instead of 8 (dark shade)
  const darkShade = getPrimaryShade(theme, 'dark');
  console.log('Dark mode shade:', darkShade); // Expected: 8, Actual: 6
  
  return <div>Check console</div>;
}
```

### Expected behavior

- When `colorScheme` is `'light'`, the function should return `theme.primaryShade.light`
- When `colorScheme` is `'dark'`, the function should return `theme.primaryShade.dark`

Currently it's returning the opposite values, which makes all components use incorrect color shades for their respective color schemes.

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
