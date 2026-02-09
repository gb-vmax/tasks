# Bug Report

### Describe the bug

When using `AppShell` with a collapsed footer in `static` mode, the footer offset is not being set correctly. The footer offset should be set to `0px !important` when the footer is collapsed in static mode, but currently this only happens in `fixed` mode.

### Reproduction

```tsx
import { AppShell } from '@mantine/core';

function App() {
  return (
    <AppShell
      footer={{ height: 60, collapsed: true }}
      layout="default"
    >
      <AppShell.Footer>Footer content</AppShell.Footer>
      <AppShell.Main>Main content</AppShell.Main>
    </AppShell>
  );
}
```

When the footer is collapsed and the layout mode is `static`, the `--app-shell-footer-offset` CSS variable is not being reset to `0px`, causing layout issues where the main content area doesn't expand properly to fill the space left by the collapsed footer.

### Expected behavior

The footer offset should be set to `0px !important` when `footer.collapsed` is true, regardless of whether the mode is `fixed` or `static`. This ensures that the layout adjusts correctly when the footer is hidden.

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
