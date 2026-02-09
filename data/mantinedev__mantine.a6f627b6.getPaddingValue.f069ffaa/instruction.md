# Bug Report

### Describe the bug

I'm experiencing an issue with AppShell padding when using negative values. When I try to set a negative padding value (like `-10` or `-20`), it gets converted to `'0'` instead of being handled properly or throwing an error.

### Reproduction

```jsx
import { AppShell } from '@mantine/core';

function Demo() {
  return (
    <AppShell padding={-10}>
      {/* Content */}
    </AppShell>
  );
}
```

When I pass a negative padding value, it's being treated the same as `0` and converted to `getSpacing('0')`. This seems incorrect - negative padding values should either be preserved as-is, rejected, or handled differently than zero.

### Expected behavior

Negative padding values should either:
1. Be passed through to `getSpacing()` as-is (allowing the spacing function to handle them)
2. Throw a validation error
3. Be explicitly documented as unsupported

Currently they're being silently converted to zero which makes debugging difficult.

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
