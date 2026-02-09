# Bug Report

### Describe the bug

When using components with the `radius` prop and passing `undefined`, the default radius is not being applied correctly. Instead of using the default radius value, the component seems to be using a different radius value than expected.

### Reproduction

```jsx
import { Button } from '@mantine/core';

function Demo() {
  return (
    <Button radius={undefined}>
      Click me
    </Button>
  );
}
```

When `radius` is explicitly set to `undefined`, the button should use the default radius (`var(--mantine-radius-default)`), but it appears to be using a different value instead.

### Expected behavior

Components should fall back to `var(--mantine-radius-default)` when the `radius` prop is `undefined`. This was the previous behavior and is consistent with how other Mantine components handle undefined prop values.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
