# Bug Report

### Describe the bug

The AppShell navbar is not displaying correctly when using responsive breakpoints in static mode. When the navbar is set to be collapsed at certain breakpoints, it appears to be completely hidden instead of properly handling the layout transition.

### Reproduction

```jsx
import { AppShell } from '@mantine/core';

function Demo() {
  return (
    <AppShell
      navbar={{
        width: { base: 300, sm: 0 },
        breakpoint: 'sm',
      }}
    >
      <AppShell.Navbar>
        {/* Navbar content */}
      </AppShell.Navbar>
      <AppShell.Main>
        {/* Main content */}
      </AppShell.Main>
    </AppShell>
  );
}
```

### Expected behavior

When the navbar width is set to 0 at the `sm` breakpoint in static mode, the navbar should collapse and the main content area should expand to fill the space. The navbar element should still be in the DOM but not visible, allowing for smooth transitions and proper grid layout adjustments.

### Actual behavior

The navbar appears to be completely removed from the layout (display: none), which causes issues with the grid column structure and prevents smooth transitions between breakpoints.

### System Info

- @mantine/core version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
