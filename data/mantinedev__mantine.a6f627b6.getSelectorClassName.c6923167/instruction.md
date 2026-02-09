# Bug Report

### Describe the bug

When using the `unstyled` prop on Mantine components, the styles are still being applied instead of being removed. Setting `unstyled={true}` should remove all default styles, but the component continues to render with the library's default CSS classes.

### Reproduction

```jsx
import { Button } from '@mantine/core';

function App() {
  return (
    <Button unstyled={true}>
      Click me
    </Button>
  );
}
```

### Expected behavior

When `unstyled` is set to `true`, the component should not have any default Mantine CSS classes applied. The button should render without any styling from the library.

### Actual behavior

The component still has the default Mantine classes applied and renders with the library styles, even though `unstyled={true}` is explicitly set.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
