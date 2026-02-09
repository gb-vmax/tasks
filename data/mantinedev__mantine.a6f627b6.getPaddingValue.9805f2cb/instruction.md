# Bug Report

### Describe the bug

When using `AppShell` with a padding value of `0`, the padding is being set to `'0'` instead of `'0px'`. This causes inconsistent CSS output and can lead to layout issues since CSS expects units for padding values in certain contexts.

### Reproduction

```jsx
import { AppShell } from '@mantine/core';

function Demo() {
  return (
    <AppShell padding={0}>
      {/* Content */}
    </AppShell>
  );
}
```

When inspecting the generated styles, the padding is set to `'0'` without the `px` unit, which differs from the expected behavior of other numeric padding values that include units.

### Expected behavior

When `padding={0}` is passed to AppShell, it should render as `'0px'` to maintain consistency with how other numeric values are handled and to ensure proper CSS formatting.

### System Info

- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
