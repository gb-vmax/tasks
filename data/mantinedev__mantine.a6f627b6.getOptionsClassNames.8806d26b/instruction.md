# Bug Report

### Describe the bug

I'm experiencing an issue with the Styles API where `classNames` from component options are not being applied correctly. When I pass custom `classNames` through the component's options prop, they seem to be ignored or overridden unexpectedly.

### Reproduction

```tsx
import { Button } from '@mantine/core';

function Demo() {
  return (
    <Button
      classNames={{
        root: 'custom-button-root',
        label: 'custom-button-label'
      }}
    >
      Click me
    </Button>
  );
}
```

The custom class names don't get applied to the button elements. Instead, only the default Mantine classes are present in the DOM.

### Expected behavior

The custom `classNames` passed through the options should be merged with the default classes and applied to the respective elements. Both `custom-button-root` and `custom-button-label` should appear in the rendered output.

### System Info
- @mantine/core version: 7.x
- React version: 18.x
- Browser: Firefox 121

---
Repository: /testbed
