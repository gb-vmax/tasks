# Bug Report

### Describe the bug

I'm experiencing an issue with the AppShell navbar behavior when using `mode="fixed"`. The navbar offset and grid width variables are not being set correctly based on the mode, causing layout issues.

### Reproduction

```jsx
import { AppShell } from '@mantine/core';

function App() {
  return (
    <AppShell
      navbar={{
        width: { base: 300, md: 400 },
        breakpoint: 'sm',
        collapsed: { mobile: true }
      }}
      mode="fixed"
    >
      <AppShell.Navbar>Navbar content</AppShell.Navbar>
      <AppShell.Main>Main content</AppShell.Main>
    </AppShell>
  );
}
```

When the navbar is collapsed on mobile breakpoints with `mode="fixed"`, the offset isn't being reset to `0px` as expected. Instead, the behavior seems inverted - the offset is being set to `0px` when mode is `static` rather than when it's `fixed`.

Additionally, the grid width variable (`--app-shell-navbar-grid-width`) is now being set regardless of the mode, when it should only be set for `static` mode.

### Expected behavior

- When `mode="fixed"`, the navbar offset should be set to `0px` on collapsed breakpoints
- When `mode="static"`, the grid width variable should be set, but the offset behavior should differ
- The CSS variables should be applied correctly based on the navbar mode to ensure proper layout

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
