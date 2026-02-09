# Bug Report

### Describe the bug

I'm experiencing an issue with `AppShell` component where passing a simple number or string value for size properties (like `navbar`, `aside`, `header`, etc.) causes the component to break. It seems like the size values are not being handled correctly anymore.

### Reproduction

```jsx
import { AppShell } from '@mantine/core';

function Demo() {
  return (
    <AppShell
      navbar={{ width: 300 }}  // This works fine
      header={{ height: 60 }}   // This works fine
    >
      {/* content */}
    </AppShell>
  );
}

// But this doesn't work:
function Demo2() {
  return (
    <AppShell
      navbar={{ width: 300 }}
      aside={{ width: 200 }}  // Simple number value doesn't work
    >
      {/* content */}
    </AppShell>
  );
}
```

When I try to use a non-object size value (just a plain number or string), the component doesn't render the section at all. It seems like the base size calculation is returning `undefined` when it shouldn't.

### Expected behavior

Both object-based responsive sizes and simple number/string values should work correctly. The component should accept both formats:
- `{ width: 300 }` - object format
- `300` - simple value format

The simple value format used to work in previous versions but seems broken now.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
