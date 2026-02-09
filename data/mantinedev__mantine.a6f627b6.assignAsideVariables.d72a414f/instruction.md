# Bug Report

### Describe the bug

The AppShell aside component is not collapsing correctly on mobile devices. When `collapsed.mobile` is set to true, the aside remains visible on mobile viewports instead of being hidden as expected.

### Reproduction

```jsx
import { AppShell } from '@mantine/core';

function Demo() {
  return (
    <AppShell
      aside={{
        width: 300,
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

When the viewport is below the `sm` breakpoint and `collapsed.mobile` is set to `true`, the aside should be hidden/collapsed. Instead, it remains visible on mobile screens.

### Additional context

The issue appears to be related to how the breakpoint media queries are being calculated for the mobile collapsed state. The aside visibility behavior works correctly on desktop but not on mobile viewports.

---
Repository: /testbed
