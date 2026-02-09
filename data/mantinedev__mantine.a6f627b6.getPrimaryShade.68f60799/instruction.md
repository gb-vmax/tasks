# Bug Report

### Describe the bug

The primary shade selection is returning the wrong shade when switching between light and dark color schemes. When the app is in dark mode, it's using the light shade value, and when in light mode, it's using the dark shade value - basically the opposite of what should happen.

### Reproduction

```tsx
import { MantineProvider, Button, useMantineTheme, useMantineColorScheme } from '@mantine/core';

function TestComponent() {
  const theme = useMantineTheme();
  const { colorScheme } = useMantineColorScheme();
  
  // In dark mode, this shows the light shade value instead of dark
  console.log('Current color scheme:', colorScheme);
  console.log('Primary shade being used:', theme.primaryShade);
  
  return <Button>Test Button</Button>;
}

// Set up theme with different shades
<MantineProvider theme={{
  primaryShade: { light: 6, dark: 8 }
}}>
  <TestComponent />
</MantineProvider>
```

### Expected behavior

When `colorScheme` is set to `'dark'`, the primary shade should use `theme.primaryShade.dark` (8 in the example).
When `colorScheme` is set to `'light'`, the primary shade should use `theme.primaryShade.light` (6 in the example).

Currently it's doing the reverse - dark mode uses the light shade and light mode uses the dark shade.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: All browsers affected

---
Repository: /testbed
