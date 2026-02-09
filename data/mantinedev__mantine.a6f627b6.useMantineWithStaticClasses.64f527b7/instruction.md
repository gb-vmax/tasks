# Bug Report

### Describe the bug

The `withStaticClasses` prop behavior seems to be inverted in MantineProvider. When I set `withStaticClasses={true}`, the components behave as if it's set to `false`, and vice versa.

### Reproduction

```jsx
import { MantineProvider, Button } from '@mantine/core';

function App() {
  return (
    <MantineProvider withStaticClasses={true}>
      <Button>Click me</Button>
    </MantineProvider>
  );
}
```

When `withStaticClasses` is explicitly set to `true`, I expect static classes to be applied to components. However, they're not being added. If I set it to `false`, then static classes ARE being applied, which is the opposite of what should happen.

### Expected behavior

- When `withStaticClasses={true}`, components should have static classes applied
- When `withStaticClasses={false}`, components should NOT have static classes applied

Currently experiencing the opposite behavior.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
