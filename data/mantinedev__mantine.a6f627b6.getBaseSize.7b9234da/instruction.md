# Bug Report

### Describe the bug

I'm experiencing an issue with `AppShell` component where passing a simple size value (string or number) causes the application to crash with a "Cannot read properties of undefined" error. This seems to be related to how the component handles non-object size values.

### Reproduction

```tsx
import { AppShell } from '@mantine/core';

function App() {
  return (
    <AppShell
      navbar={{ width: 300, breakpoint: 'sm' }}
      padding="md"
    >
      {/* Content */}
    </AppShell>
  );
}
```

When using a numeric or string value directly for width (e.g., `width: 300` or `width: '300px'`), the component throws an error trying to access `.base` property on a primitive value.

### Expected behavior

The component should accept both simple values (strings/numbers) and responsive size objects without errors. Simple values should be treated as the base size.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
