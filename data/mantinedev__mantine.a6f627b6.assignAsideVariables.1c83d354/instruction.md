# Bug Report

### Describe the bug

The AppShell aside component is not behaving correctly with the `collapsed.mobile` prop. When `collapsed.mobile` is set to `false`, the aside appears to be hidden on mobile viewports instead of being visible. Conversely, when `collapsed.mobile` is `true`, the aside shows up when it should be collapsed.

The behavior seems inverted - it's doing the opposite of what the prop value indicates.

### Reproduction

```tsx
import { AppShell } from '@mantine/core';

function App() {
  return (
    <AppShell
      aside={{
        width: 300,
        breakpoint: 'sm',
        collapsed: { mobile: false } // Expecting aside to be visible on mobile
      }}
    >
      <AppShell.Aside>
        Aside content
      </AppShell.Aside>
      <AppShell.Main>
        Main content
      </AppShell.Main>
    </AppShell>
  );
}
```

**Expected:** The aside should be visible on mobile when `collapsed.mobile: false`

**Actual:** The aside is hidden on mobile when `collapsed.mobile: false`

Additionally, there seems to be an issue with the `mode` prop where setting it to `'fixed'` doesn't apply the correct offset styles, while other modes do.

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox
- Device: Mobile viewport (< sm breakpoint)

---
Repository: /testbed
