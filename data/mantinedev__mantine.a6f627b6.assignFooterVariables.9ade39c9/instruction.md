# Bug Report

### Describe the bug
I'm experiencing an issue with the AppShell footer where the offset and height variables are not being applied correctly. The footer appears to be rendering in unexpected positions and the spacing seems completely off.

### Reproduction
```jsx
import { AppShell } from '@mantine/core';

function Demo() {
  return (
    <AppShell
      footer={{ height: 60 }}
    >
      <AppShell.Footer>Footer content</AppShell.Footer>
      <AppShell.Main>Main content</AppShell.Main>
    </AppShell>
  );
}
```

When I set a footer height, the footer offset variable doesn't seem to be calculated properly. The main content area overlaps with the footer instead of being properly spaced.

Also tried with responsive heights:
```jsx
<AppShell
  footer={{ 
    height: { base: 60, sm: 80, md: 100 }
  }}
>
```

The responsive sizing also behaves strangely - it seems like the base height is being set at media query breakpoints instead of being the default.

### Expected behavior
The footer should have proper offset applied so content doesn't overlap. When using responsive heights, the base height should be the default and only change at the specified breakpoints.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120
- OS: macOS

---
Repository: /testbed
