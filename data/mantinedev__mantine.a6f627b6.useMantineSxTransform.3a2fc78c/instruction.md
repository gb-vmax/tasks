# Bug Report

### Describe the bug

I'm getting a runtime error when using Mantine components after updating to the latest version. The error occurs during rendering and appears to be related to the `stylesTransform` context.

The error message is:
```
Cannot read properties of undefined (reading 'call')
```

or similar errors about undefined values being called as functions.

### Reproduction

```jsx
import { MantineProvider } from '@mantine/core';

function App() {
  return (
    <MantineProvider>
      <YourComponent />
    </MantineProvider>
  );
}
```

When rendering any Mantine component inside the provider, the application crashes with the error mentioned above.

### Expected behavior

Components should render normally without throwing errors. This was working fine in previous versions.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

This seems to have started happening recently, possibly after a recent update. Let me know if you need more details to reproduce!

---
Repository: /testbed
