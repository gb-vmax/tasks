# Bug Report

### Describe the bug

I'm experiencing issues with `AppShell` padding when using responsive size values. The padding doesn't seem to be applied correctly at different breakpoints.

### Reproduction

```jsx
import { AppShell } from '@mantine/core';

function Demo() {
  return (
    <AppShell
      padding={{
        base: 'md',
        sm: 'lg',
        lg: 'xl'
      }}
    >
      {/* Content */}
    </AppShell>
  );
}
```

When I set responsive padding values like above, the base padding value gets applied to the media query styles instead of staying as the base/default value. The breakpoint-specific values (sm, lg) don't get applied at all.

### Expected behavior

- The `base` value should be applied as the default padding
- The breakpoint values (`sm`, `lg`, etc.) should override the base padding at their respective breakpoints

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
