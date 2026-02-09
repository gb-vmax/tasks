# Bug Report

### Describe the bug

When passing an array of `classNames` to a component, the styling breaks completely. It seems like array-type classNames are not being handled correctly and the classes aren't being applied to the component.

### Reproduction

```tsx
import { Button } from '@mantine/core';

const customClasses = {
  root: 'my-custom-root',
  label: 'my-custom-label'
};

// This doesn't work - classes are not applied
<Button classNames={[customClasses]}>
  Click me
</Button>

// Expected to work the same as:
<Button classNames={customClasses}>
  Click me
</Button>
```

### Expected behavior

When `classNames` is provided as an array (even with a single object inside), the classes should still be properly merged and applied to the component elements. The component should render with the custom classes applied.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
