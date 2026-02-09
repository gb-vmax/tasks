# Bug Report

### Describe the bug

I'm experiencing an issue with the `AppShell` component where the aside panel is not displaying correctly at different breakpoints. The aside seems to be visible/hidden at the wrong screen sizes, and the responsive behavior appears to be inverted from what's expected.

### Reproduction

```tsx
import { AppShell } from '@mantine/core';

function Demo() {
  return (
    <AppShell
      aside={{
        width: { base: 300, sm: 350, lg: 400 },
        breakpoint: 'sm',
        collapsed: { mobile: true, desktop: false }
      }}
    >
      <AppShell.Aside>Aside content</AppShell.Aside>
      <AppShell.Main>Main content</AppShell.Main>
    </AppShell>
  );
}
```

When I set up the aside with responsive widths like above:
1. On mobile (below `sm` breakpoint), the aside appears even though `collapsed.mobile` is set to `true`
2. On desktop (above `sm` breakpoint), the aside behavior doesn't match expectations
3. The aside width seems to only apply at the base breakpoint instead of at the specified responsive breakpoints

### Expected behavior

- The aside should be collapsed on mobile when `collapsed.mobile: true`
- The aside width should apply at the correct breakpoints (not just base)
- The layout should adjust properly based on the breakpoint configuration

### System Info

- @mantine/core version: latest
- Browser: Chrome/Firefox
- Device: Desktop and mobile testing

---
Repository: /testbed
