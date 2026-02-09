# Bug Report

### Describe the bug

The `useMantineWithStaticClasses` hook is returning inverted boolean values. When `withStaticClasses` is set to `true`, the hook returns `false`, and vice versa. This causes components to not apply static classes when they should, and apply them when they shouldn't.

### Reproduction

```tsx
import { MantineProvider, useMantineWithStaticClasses } from '@mantine/core';

function TestComponent() {
  const withStaticClasses = useMantineWithStaticClasses();
  console.log('withStaticClasses:', withStaticClasses);
  return null;
}

// Case 1: withStaticClasses set to true
<MantineProvider withStaticClasses={true}>
  <TestComponent />
</MantineProvider>
// Expected: true
// Actual: false

// Case 2: withStaticClasses set to false
<MantineProvider withStaticClasses={false}>
  <TestComponent />
</MantineProvider>
// Expected: false
// Actual: true
```

### Expected behavior

The hook should return the actual value of `withStaticClasses` from the provider, not the inverted value. Components relying on this hook are getting the opposite behavior of what was configured.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
