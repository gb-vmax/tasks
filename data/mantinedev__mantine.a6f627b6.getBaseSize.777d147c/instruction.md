# Bug Report

### Describe the bug

I'm experiencing an issue with the AppShell component where non-responsive sizes (simple string/number values) are not being applied correctly. When I pass a regular size value instead of a responsive object, the AppShell sections don't render with the expected dimensions.

### Reproduction

```tsx
import { AppShell } from '@mantine/core';

function Demo() {
  return (
    <AppShell
      navbar={{ width: 300 }}  // Simple number value
      header={{ height: 60 }}   // Simple number value
    >
      {/* Content */}
    </AppShell>
  );
}
```

When using simple size values like above, the navbar and header don't get their width/height applied. However, if I use the responsive object format, it works:

```tsx
<AppShell
  navbar={{ width: { base: 300 } }}  // This works
  header={{ height: { base: 60 } }}   // This works
>
```

### Expected behavior

Both simple values and responsive objects should work. Simple size values should be applied as the base size without requiring the responsive object wrapper.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
