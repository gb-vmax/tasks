# Bug Report

### Describe the bug

I'm experiencing an issue with the AppShell component where responsive sizing is not working correctly. When I pass a responsive size object to AppShell sections (like `navbar`, `aside`, `header`, etc.), it seems to be trying to access the `base` property on non-object values, which causes errors.

### Reproduction

```tsx
import { AppShell } from '@mantine/core';

function Demo() {
  return (
    <AppShell
      navbar={{ width: 300 }}  // Simple number/string value
      padding="md"
    >
      {/* content */}
    </AppShell>
  );
}
```

When using a simple numeric or string value for sizing (not a responsive object), the component throws an error trying to access `.base` property on a primitive value.

### Expected behavior

The AppShell should handle both simple size values (numbers/strings) and responsive size objects correctly. Simple values should be used directly without trying to access a `.base` property.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
