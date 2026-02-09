# Bug Report

### Describe the bug

When using components with `unstyled` prop set to `true`, focus styles are still being applied. According to the documentation, the `unstyled` prop should remove all default styles including focus rings, but currently focus classes are still added to focusable elements even when `unstyled={true}`.

### Reproduction

```jsx
import { Button } from '@mantine/core';

function Demo() {
  return (
    <Button unstyled focusable>
      Click me
    </Button>
  );
}
```

When the button is focused, it still receives focus ring styles even though `unstyled` is set to `true`.

### Expected behavior

When `unstyled={true}` is passed to a component, no focus styles should be applied. The component should be completely unstyled including focus rings and active states.

### Additional context

This affects any focusable component when using the `unstyled` prop. The focus ring classes are being added regardless of the `unstyled` setting.

---
Repository: /testbed
