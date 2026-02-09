# Bug Report

### Describe the bug

When using custom `classNames` prop with component selectors, the class names are not being applied correctly. The resolved class names seem to be returning `undefined` or an incorrect structure, causing styles to not be applied to the targeted elements.

### Reproduction

```jsx
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

When trying to apply custom class names to specific selectors (like `label`, `inner`, etc.), the classes are not being applied. Only works inconsistently or not at all.

### Expected behavior

The `classNames` prop should correctly apply the specified class names to their corresponding component parts/selectors. Each selector should receive its designated class name.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
