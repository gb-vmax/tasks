# Bug Report

### Describe the bug

The AppShell aside panel is not displaying correctly at different breakpoints. The aside width and offset variables seem to be applied to the wrong breakpoint, and the collapse behavior appears inverted - the aside is hidden when it should be visible and vice versa.

### Reproduction

```tsx
import { AppShell } from '@mantine/core';

function Demo() {
  return (
    <AppShell
      aside={{
        width: { base: 300, sm: 400 },
        breakpoint: 'sm',
        collapsed: { desktop: false }
      }}
    >
      <AppShell.Aside>Aside content</AppShell.Aside>
      <AppShell.Main>Main content</AppShell.Main>
    </AppShell>
  );
}
```

### Expected behavior

- The aside should have width 300px at base breakpoint and 400px at sm breakpoint
- When `collapsed.desktop` is `false`, the aside should be visible on desktop screens
- The aside width CSS variables should be applied to the correct responsive breakpoints

### Actual behavior

- The aside width appears to only be applied at the base breakpoint, not at other breakpoints
- The aside seems to be collapsed when `collapsed.desktop` is set to `false`
- The layout doesn't respond correctly to breakpoint changes

### System Info

- @mantine/core version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
