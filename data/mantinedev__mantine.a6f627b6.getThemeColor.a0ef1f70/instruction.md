# Bug Report

### Describe the bug

I'm experiencing an issue with theme colors not being applied correctly. When using colors from the theme configuration, the actual color values are not being rendered properly in the components.

### Reproduction

```jsx
import { MantineProvider, Button } from '@mantine/core';

function App() {
  return (
    <MantineProvider theme={{ primaryColor: 'blue' }}>
      <Button color="blue">Click me</Button>
    </MantineProvider>
  );
}
```

When inspecting the rendered button, instead of seeing the CSS variable reference (like `var(--mantine-color-blue-6)`), I'm seeing the raw color string value. This breaks the theming system and prevents proper color application.

### Expected behavior

The `getThemeColor` function should return CSS variable references (e.g., `var(--mantine-color-blue-6)`) when a theme color is used, allowing the browser to properly resolve the color value from the CSS custom properties.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120
- OS: macOS

---
Repository: /testbed
