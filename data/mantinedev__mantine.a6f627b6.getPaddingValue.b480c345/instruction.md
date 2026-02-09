# Bug Report

### Describe the bug

I'm experiencing an issue with AppShell padding values. When I try to set padding to a non-zero value, it's being ignored and treated as `0` instead. Conversely, when I explicitly set padding to `0`, it seems to be applying some spacing value.

### Reproduction

```jsx
import { AppShell } from '@mantine/core';

// This should apply padding but renders with 0 padding
<AppShell padding="md">
  <AppShell.Main>
    Content here
  </AppShell.Main>
</AppShell>

// This should have no padding but gets spacing applied
<AppShell padding={0}>
  <AppShell.Main>
    Content here
  </AppShell.Main>
</AppShell>
```

### Expected behavior

- When `padding="md"` or any non-zero value is provided, the AppShell should apply the corresponding spacing
- When `padding={0}` is provided, the AppShell should have no padding (0px)

### Current behavior

The behavior appears to be inverted - zero padding values get spacing applied, while non-zero padding values result in 0 padding.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
