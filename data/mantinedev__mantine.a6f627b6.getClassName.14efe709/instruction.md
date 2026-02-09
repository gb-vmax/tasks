# Bug Report

### Describe the bug

I'm experiencing an issue with className generation in Mantine components. It seems like some class names are not being applied correctly to components, particularly when using custom `classNames` prop with transformed styles.

### Reproduction

```tsx
import { Button } from '@mantine/core';

function Demo() {
  return (
    <Button
      classNames={{
        root: 'custom-root',
        label: 'custom-label'
      }}
    >
      Click me
    </Button>
  );
}
```

When inspecting the rendered component, I notice that the custom class names from the `classNames` prop are being applied twice to the same element, which causes styling conflicts and unexpected behavior.

### Expected behavior

Each className should only be applied once. The component should respect the `classNames` prop without duplicating class names in the final output.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

This seems to have started happening recently. The class names appear to be getting merged incorrectly somewhere in the styles API.

---
Repository: /testbed
