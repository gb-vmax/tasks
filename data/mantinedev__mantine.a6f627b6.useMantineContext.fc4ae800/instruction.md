# Bug Report

### Describe the bug

After updating to the latest version, I'm getting an error `[@mantine/core] MantineProvider was not found in tree` even though my components are properly wrapped with `MantineProvider`. This is happening on components that were working fine before.

### Reproduction

```jsx
import { MantineProvider, Button } from '@mantine/core';

function App() {
  return (
    <MantineProvider>
      <Button>Click me</Button>
    </MantineProvider>
  );
}
```

When rendering the Button component (or any other Mantine component), the error is thrown immediately even though the MantineProvider is clearly present in the component tree.

### Expected behavior

Components wrapped in MantineProvider should work without throwing errors about the provider not being found.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
