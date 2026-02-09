# Bug Report

### Describe the bug

I'm getting an error when trying to use Mantine components in my app. The error says `[@mantine/core] MantineProvider was not found in tree` even though I have the `MantineProvider` properly wrapped around my component tree.

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

When I render this component, I get the error thrown immediately. The component doesn't render at all.

### Expected behavior

The Button component should render normally without any errors when wrapped in MantineProvider.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
