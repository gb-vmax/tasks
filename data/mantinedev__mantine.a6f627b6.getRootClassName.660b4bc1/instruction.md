# Bug Report

### Describe the bug

I'm experiencing an issue with the Styles API where class names are being applied incorrectly to component elements. It seems like the root element is not receiving its className properly, while non-root elements are getting classes they shouldn't have.

### Reproduction

```tsx
import { Button } from '@mantine/core';

function Demo() {
  return (
    <Button 
      classNames={{
        root: 'my-custom-root-class',
        label: 'my-custom-label-class'
      }}
    >
      Click me
    </Button>
  );
}
```

When inspecting the rendered output:
- The root element (button) is missing `my-custom-root-class`
- The label element appears to have the wrong class applied

### Expected behavior

The root selector should receive the className when the selector matches the root. Non-root selectors should receive their respective classNames only when they match their specific selectors.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

This seems to have started happening recently. The className assignment logic appears to be inverted somehow.

---
Repository: /testbed
