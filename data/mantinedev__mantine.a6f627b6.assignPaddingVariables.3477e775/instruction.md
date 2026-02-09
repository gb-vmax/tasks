# Bug Report

### Describe the bug

I'm experiencing an issue with AppShell padding configuration when using responsive sizing. The padding values are not being applied correctly across different breakpoints.

### Reproduction

```jsx
import { AppShell } from '@mantine/core';

function App() {
  return (
    <AppShell
      padding={{ base: 'md', sm: 'lg', md: 'xl' }}
    >
      {/* content */}
    </AppShell>
  );
}
```

When I use responsive padding values like above, the base padding value doesn't get applied at all. Instead, the breakpoint-specific values (sm, md, etc.) seem to be taking precedence even on the base viewport size.

### Expected behavior

The `base` padding value should be applied as the default padding, and the breakpoint-specific values should override it at their respective screen sizes. Currently it seems like the base value is being ignored and only the breakpoint values are being used.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
