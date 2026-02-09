# Bug Report

### Describe the bug

Focus ring styles are not being applied to focusable components when using the default styling. The focus indicator disappears completely when interacting with buttons, inputs, and other focusable elements.

### Reproduction

```jsx
import { Button } from '@mantine/core';

function Demo() {
  return (
    <Button>Click me and try to focus</Button>
  );
}
```

Steps to reproduce:
1. Create a button or any focusable component with default Mantine styling
2. Click on the button and observe the focus state
3. The focus ring is not visible even though the element is focused

### Expected behavior

Focusable components should display the theme's focus ring styles (e.g., the blue outline) when focused. This worked correctly in previous versions.

### Additional context

This seems to affect all components that use the `focusable` option in the styles API. The focus styles are completely missing unless custom focus classes are explicitly provided.

---
Repository: /testbed
