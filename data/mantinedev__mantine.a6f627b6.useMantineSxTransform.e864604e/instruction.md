# Bug Report

### Describe the bug

After a recent update, I'm getting a runtime error when using Mantine components. The application crashes with a TypeError related to accessing properties on the context object.

### Reproduction

```jsx
import { Button } from '@mantine/core';

function App() {
  return (
    <MantineProvider>
      <Button>Click me</Button>
    </MantineProvider>
  );
}
```

When rendering any Mantine component inside `MantineProvider`, the app throws an error. It seems like there's an issue with how the context is being accessed internally.

### Expected behavior

The component should render normally without any errors. This was working fine in the previous version.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
