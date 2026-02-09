# Bug Report

### Describe the bug

I'm experiencing an issue where custom classNames are not being applied correctly to components. It seems like the selector and stylesCtx parameters are getting mixed up somehow, causing the wrong classes to be resolved.

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

When inspecting the rendered component, the classNames are either not applied at all or applied to the wrong elements. For example, the `root` class might end up on the `label` element and vice versa.

### Expected behavior

The classNames should be applied to their corresponding selectors. The `root` className should be applied to the root element, and the `label` className should be applied to the label element.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
