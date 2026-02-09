# Bug Report

### Describe the bug

When using `useMantineClassNamesPrefix()` hook, I'm getting a runtime error when the `MantineProvider` is not properly configured or when `settings` is undefined. The hook tries to access `classNamesPrefix` directly without checking if `settings` exists first.

### Reproduction

```tsx
import { useMantineClassNamesPrefix } from '@mantine/core';

function MyComponent() {
  // This throws an error when settings is undefined
  const prefix = useMantineClassNamesPrefix();
  
  return <div>Prefix: {prefix}</div>;
}
```

### Expected behavior

The hook should safely handle cases where `settings` might be undefined and return `undefined` or a default value instead of throwing an error.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
