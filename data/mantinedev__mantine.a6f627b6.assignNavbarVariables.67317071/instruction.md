# Bug Report

### Describe the bug

The AppShell navbar is not displaying correctly at different breakpoints. The navbar width and offset CSS variables seem to be applied at the wrong media query breakpoints, causing the layout to break.

### Reproduction

```tsx
import { AppShell } from '@mantine/core';

function Demo() {
  return (
    <AppShell
      navbar={{
        width: { base: 200, sm: 300, lg: 400 },
        breakpoint: 'sm',
        collapsed: { mobile: true }
      }}
    >
      <AppShell.Navbar>Navbar content</AppShell.Navbar>
      <AppShell.Main>Main content</AppShell.Main>
    </AppShell>
  );
}
```

### Expected behavior

- The navbar should respect the width values at each breakpoint (200px base, 300px at sm, 400px at lg)
- When collapsed on mobile, the navbar should properly hide/show at the correct breakpoint threshold
- The CSS variables `--app-shell-navbar-width` and `--app-shell-navbar-offset` should be applied at the appropriate media queries

### Actual behavior

The navbar widths are being applied at incorrect breakpoints. It appears the base width is not being set properly, and the mobile collapse breakpoint calculation seems off by a small amount, causing the navbar to collapse/expand at slightly the wrong viewport size.

### System Info

- @mantine/core version: latest
- Browser: All browsers affected

---
Repository: /testbed
