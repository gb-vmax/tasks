# Bug Report

### Describe the bug

I'm getting an error when trying to use a valid primary color in my Mantine theme configuration. The theme validation is throwing `INVALID_PRIMARY_COLOR_ERROR` even though the color exists in the theme's color palette.

### Reproduction

```js
import { MantineProvider, createTheme } from '@mantine/core';

const theme = createTheme({
  primaryColor: 'blue',
  colors: {
    blue: [ /* valid color array */ ],
    red: [ /* valid color array */ ]
  }
});

// This throws an error about invalid primary color
<MantineProvider theme={theme}>
  <App />
</MantineProvider>
```

### Expected behavior

The theme should be accepted without errors when `primaryColor` is set to a color that exists in the `colors` object. In this case, 'blue' is defined in `theme.colors`, so it should be valid.

### Additional context

This seems to have started happening recently. Previously, this exact configuration worked fine. The error message suggests the primary color is invalid, but I've verified that the color key definitely exists in the colors object.

---
Repository: /testbed
