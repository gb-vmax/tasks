# Bug Report

### Describe the bug

When using `AppShell` with padding set to `0`, the padding value is being returned as `'0'` instead of `'0px'`. This causes inconsistent behavior with CSS units and may break layouts that expect proper unit values.

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

When padding is set to `0`, the component should output `'0px'` as the padding value, but it's currently returning just `'0'` without the unit.

### Expected behavior

When padding is explicitly set to `0`, it should return `'0px'` to maintain consistency with other numeric padding values and proper CSS unit formatting.

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
