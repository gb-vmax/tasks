# Bug Report

### Describe the bug

When using the `unstyled` prop on Mantine components, the component classes are still being applied instead of being removed. The `unstyled` prop should remove all default styling, but the library CSS classes are still present in the rendered output.

### Reproduction

```jsx
import { Button } from '@mantine/core';

function App() {
  return (
    <Button unstyled>
      Click me
    </Button>
  );
}
```

### Expected behavior

When `unstyled={true}` is set, the component should not have any library CSS classes applied. The element should be rendered without the default Mantine styling classes.

### Actual behavior

The component still receives the CSS classes from the library's module styles even when `unstyled` is true. This prevents proper customization when trying to build completely custom styled components.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: All browsers

---
Repository: /testbed
