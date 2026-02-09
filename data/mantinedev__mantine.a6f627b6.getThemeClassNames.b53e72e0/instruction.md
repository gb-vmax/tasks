# Bug Report

### Describe the bug

There's an issue with how theme class names are being resolved in nested component structures. When using `classNames` prop with theme-level component configuration, the class names are being applied to the wrong elements.

### Reproduction

```jsx
import { MantineProvider, Button } from '@mantine/core';

const theme = {
  components: {
    Button: {
      classNames: {
        root: 'custom-button-root',
        label: 'custom-button-label'
      }
    }
  }
};

function App() {
  return (
    <MantineProvider theme={theme}>
      <Button>Click me</Button>
    </MantineProvider>
  );
}
```

In this setup, the class names seem to be getting mixed up - the `root` class is being applied where `label` should be, and vice versa. The component renders but the styling is completely wrong because classes are on the wrong DOM elements.

### Expected behavior

The theme-level `classNames` should be correctly mapped to their corresponding component parts. `root` classes should go to the root element, `label` classes to the label element, etc.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
