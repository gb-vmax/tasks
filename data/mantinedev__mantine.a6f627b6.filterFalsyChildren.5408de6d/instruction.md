# Bug Report

### Describe the bug

When using `Group` component with conditional children, some falsy values like `null` and `undefined` are not being filtered out correctly. This causes issues with layout and spacing as these falsy children are still being rendered or counted.

### Reproduction

```jsx
import { Group, Button } from '@mantine/core';

function MyComponent() {
  const showButton = false;
  
  return (
    <Group>
      <Button>First</Button>
      {showButton && <Button>Conditional</Button>}
      {null}
      {undefined}
      <Button>Last</Button>
    </Group>
  );
}
```

The `null` and `undefined` values should be filtered out but they're affecting the Group's layout/spacing behavior.

### Expected behavior

All falsy values (including `null`, `undefined`, and `false`) should be filtered from children and not affect the Group component's rendering or spacing.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
