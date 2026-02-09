# Bug Report

### Describe the bug

I'm experiencing an issue with the Styles API where `classNames` from component options are not being applied correctly. When I pass `classNames` through component options, they don't seem to be picked up and the styling breaks.

### Reproduction

```jsx
import { Button } from '@mantine/core';

function Demo() {
  return (
    <Button
      classNames={{
        root: 'my-custom-class'
      }}
    >
      Click me
    </Button>
  );
}
```

The custom class name should be applied to the button root element, but it's not showing up in the rendered output.

### Expected behavior

When passing `classNames` via component props or options, they should be properly resolved and applied to the corresponding component parts. The custom classes should appear in the DOM.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
