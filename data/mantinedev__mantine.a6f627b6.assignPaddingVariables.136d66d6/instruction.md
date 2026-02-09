# Bug Report

### Describe the bug

When using `AppShell` with responsive padding configuration, the padding values are not being applied correctly at different breakpoints. The padding seems to only work when a `base` value is provided, and even then the behavior is inconsistent.

### Reproduction

```jsx
import { AppShell } from '@mantine/core';

function Demo() {
  return (
    <AppShell
      padding={{ xs: 'md', sm: 'lg', md: 'xl' }}
    >
      {/* Content */}
    </AppShell>
  );
}
```

When using responsive padding without a `base` value, the padding doesn't get applied at the specified breakpoints. The `--app-shell-padding` CSS variable is not being set properly in the media queries.

### Expected behavior

The `AppShell` component should apply the correct padding values at each breakpoint regardless of whether a `base` value is provided. Each breakpoint (xs, sm, md, etc.) should independently set the appropriate padding.

For example:
```jsx
// This should work
<AppShell padding={{ xs: 'md', sm: 'lg' }}>

// This should also work  
<AppShell padding={{ base: 'sm', md: 'xl' }}>

// And this too
<AppShell padding="md">
```

### System Info

- @mantine/core version: 7.x
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
