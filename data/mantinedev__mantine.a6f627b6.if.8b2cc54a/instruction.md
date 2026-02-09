# Bug Report

### Describe the bug

The `isResponsiveSize` function in AppShell is incorrectly identifying non-object values as responsive sizes. When passing certain primitive values or null, the function doesn't properly validate them and can cause unexpected behavior in the AppShell component.

### Reproduction

```tsx
import { isResponsiveSize } from '@mantine/core';

// This should return false but doesn't work correctly
const result1 = isResponsiveSize(null);
const result2 = isResponsiveSize(undefined);
const result3 = isResponsiveSize(0);
const result4 = isResponsiveSize('');

// Expected: all should return false
// Actual: may not return false in all cases
```

When using AppShell with these edge case values, the component may not handle them correctly:

```tsx
<AppShell
  navbar={{ width: null }}  // Should be handled gracefully
>
  {/* content */}
</AppShell>
```

### Expected behavior

The function should correctly return `false` for all non-object values including `null`, `undefined`, numbers, strings, etc. Only actual responsive size objects should return `true`.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
