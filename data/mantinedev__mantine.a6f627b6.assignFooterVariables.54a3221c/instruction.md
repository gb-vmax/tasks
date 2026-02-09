# Bug Report

### Describe the bug

When using `AppShell` with a collapsed footer, the footer height is not being applied correctly at the base breakpoint. The `--app-shell-footer-height` CSS variable is only set for non-base media queries, which means the footer height isn't defined for the default/base viewport size.

### Reproduction

```tsx
import { AppShell } from '@mantine/core';

function Demo() {
  return (
    <AppShell
      footer={{
        height: { base: 60, sm: 80, md: 100 },
        collapsed: true
      }}
    >
      <AppShell.Footer>Footer content</AppShell.Footer>
      <AppShell.Main>Main content</AppShell.Main>
    </AppShell>
  );
}
```

### Expected behavior

The footer height should be applied at all breakpoints including the base breakpoint. The CSS variable `--app-shell-footer-height` should be set to `60px` (the base value) for viewports that don't match any other breakpoint.

### Current behavior

The footer height is only applied for `sm`, `md`, and other named breakpoints, but not for the `base` breakpoint. This causes the footer to not have the correct height on smaller viewports or when no other breakpoint matches.

### System Info

- @mantine/core version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
