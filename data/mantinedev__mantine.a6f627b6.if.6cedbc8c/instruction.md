# Bug Report

### Describe the bug

I'm experiencing an issue with the `AppShell` component where the responsive sizing logic seems to be broken. When passing size configurations to AppShell sections (like `Navbar`, `Header`, etc.), the component is not correctly identifying whether a size value is responsive or not.

### Reproduction

```tsx
import { AppShell } from '@mantine/core';

function Demo() {
  return (
    <AppShell
      navbar={{ width: 300, breakpoints: { base: 200, sm: 250 } }}
    >
      {/* Content */}
    </AppShell>
  );
}
```

When using simple numeric values or non-responsive size configurations, they're being incorrectly treated as responsive sizes. This causes the AppShell to apply wrong styles and the layout breaks.

### Expected behavior

The component should correctly distinguish between:
- Simple size values (numbers or strings)
- Responsive size objects with breakpoint configurations
- `null` or `undefined` values

Non-responsive sizes should be handled differently from responsive breakpoint configurations.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: All browsers affected

---
Repository: /testbed
