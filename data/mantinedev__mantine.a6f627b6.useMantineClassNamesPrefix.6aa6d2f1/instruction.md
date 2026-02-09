# Bug Report

### Describe the bug

The `useMantineClassNamesPrefix()` hook is returning the entire Mantine context object instead of just the `classNamesPrefix` property. This causes issues when trying to use the prefix value in components.

### Reproduction

```tsx
import { useMantineClassNamesPrefix } from '@mantine/core';

function MyComponent() {
  const prefix = useMantineClassNamesPrefix();
  
  // Expected: prefix should be a string (e.g., 'mantine')
  // Actual: prefix is the entire context object
  
  const className = `${prefix}-button`; // This doesn't work as expected
  
  return <button className={className}>Click me</button>;
}
```

### Expected behavior

The hook should return only the `classNamesPrefix` string value, not the entire context object. This would allow it to be used directly for building class names.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
