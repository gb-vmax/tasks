# Bug Report

### Describe the bug

The AppShell aside component is not collapsing correctly on mobile devices. When `collapsed.mobile` is set to true, the aside remains visible at the wrong breakpoint. It seems like the aside is hiding at breakpoints where it should be visible and showing at breakpoints where it should be hidden.

### Reproduction

```jsx
import { AppShell } from '@mantine/core';

function Demo() {
  return (
    <AppShell
      aside={{
        width: { base: 300, sm: 400 },
        breakpoint: 'sm',
        collapsed: { mobile: true }
      }}
    >
      <AppShell.Aside>Aside content</AppShell.Aside>
      <AppShell.Main>Main content</AppShell.Main>
    </AppShell>
  );
}
```

### Expected behavior

When the viewport is below the `sm` breakpoint, the aside should be collapsed/hidden. When the viewport is at or above the `sm` breakpoint, the aside should be visible.

### Actual behavior

The aside appears to be doing the opposite - it's visible on mobile (below breakpoint) and hidden on larger screens (at or above breakpoint).

### System Info

- @mantine/core version: 7.x
- Browser: Chrome/Firefox/Safari (occurs on all)
- Device: Mobile and desktop

---
Repository: /testbed
