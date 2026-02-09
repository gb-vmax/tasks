# Bug Report

### Describe the bug
When using `classNames` prop with component options, the class names are not being applied correctly. It seems like the props are not being passed through properly when `options.props` is defined, causing styles to not be applied as expected.

### Reproduction
```tsx
import { Button } from '@mantine/core';

const MyComponent = () => {
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
};
```

When trying to apply custom class names through the `classNames` prop, the classes are either not applied at all or applied incorrectly. This affects the ability to customize component styles using the Styles API.

### Expected behavior
The custom class names should be properly applied to the component elements. The `classNames` prop should work consistently regardless of whether `options.props` is provided or not.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
