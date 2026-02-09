# Bug Report

### Describe the bug

When using the `classNames` prop with Mantine components, the resolved class names are not being applied correctly. It seems like the class names are being lost or not properly merged when the component tries to apply them.

I noticed this after a recent update - components that were working fine before are now missing their custom class names. The styles that should be applied via the `classNames` prop just don't show up in the DOM.

### Reproduction

```jsx
import { Button } from '@mantine/core';

function MyComponent() {
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

When inspecting the rendered button in the browser, the custom class names (`custom-button-root` and `custom-button-label`) are not present on the respective elements.

### Expected behavior

The custom class names provided via the `classNames` prop should be applied to the corresponding elements of the component. The classes should be visible in the DOM and the associated styles should take effect.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
