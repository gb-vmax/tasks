# Bug Report

### Describe the bug

I'm experiencing an issue with the Styles API where custom `classNames` passed through component options are not being applied correctly. It seems like the properties are getting mixed up somewhere in the styling system.

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

When inspecting the rendered component, the custom class names don't appear on the expected elements. Instead, the component seems to be ignoring the `classNames` prop entirely or applying them to the wrong elements.

### Expected behavior

The custom class names should be applied to their respective component parts (root, label, etc.) as specified in the `classNames` object.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
