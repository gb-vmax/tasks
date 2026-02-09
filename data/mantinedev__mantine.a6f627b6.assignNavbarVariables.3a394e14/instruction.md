# Bug Report

### Describe the bug

When using `AppShell` with a `navbar` in static mode and responsive breakpoints, the main content area doesn't properly expand to fill the full width when the navbar is hidden at certain breakpoints. The layout appears to leave a gap where the navbar should be, as if it's still occupying space in the grid.

### Reproduction

```tsx
import { AppShell } from '@mantine/core';

function Demo() {
  return (
    <AppShell
      navbar={{
        width: { base: 300, md: 0 },
        breakpoint: 'md',
      }}
    >
      <AppShell.Navbar>Navbar content</AppShell.Navbar>
      <AppShell.Main>
        Main content - should expand to full width on md breakpoint
      </AppShell.Main>
    </AppShell>
  );
}
```

### Expected behavior

When the navbar width is set to 0 at a breakpoint (e.g., `md: 0`), the main content should expand to take up the full available width. The grid layout should collapse the navbar column completely.

### Actual behavior

The main content doesn't expand properly. There appears to be a gap or the content doesn't start from the correct grid column position when the navbar is hidden.

### System Info

- @mantine/core version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
