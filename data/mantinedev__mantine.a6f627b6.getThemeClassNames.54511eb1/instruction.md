# Bug Report

### Describe the bug

I'm experiencing an issue with the Styles API where theme class names are not being applied correctly to components. When using multiple theme names, the class names from the wrong theme components are being used, resulting in incorrect styling.

### Reproduction

```tsx
import { MantineProvider, Button } from '@mantine/core';

const theme = {
  components: {
    Button: {
      classNames: {
        root: 'custom-button-root'
      }
    },
    Input: {
      classNames: {
        root: 'custom-input-root'
      }
    }
  }
};

// When a component has multiple theme names
// The classNames are being pulled from the wrong component
<MantineProvider theme={theme}>
  <Button>Click me</Button>
</MantineProvider>
```

### Expected behavior

Components should use their own theme class names based on the theme name, not based on the index/position in the array. Each component should get the correct class names from `theme.components[themeName]`.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: All browsers

---
Repository: /testbed
