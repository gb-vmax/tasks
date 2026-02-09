# Bug Report

### Describe the bug

When using the `unstyled` prop on Mantine components, the styles are not being properly removed. The component still applies CSS classes even when `unstyled={true}` is set.

### Reproduction

```tsx
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

When `unstyled` is set to `true`, the component should not apply any default CSS classes from the library's module styles. The button should render without any Mantine styling.

### Actual behavior

The component still has CSS classes applied from the library styles even with `unstyled={true}`.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
