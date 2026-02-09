# Bug Report

### Describe the bug

The `useMantineClassNamesPrefix` hook is returning an incorrect value. It seems to be checking for `classNamePrefix` (singular) instead of `classNamesPrefix` (plural), which causes it to return `undefined` and then fallback to `prefix` instead of returning the correct `classNamesPrefix` value from the context.

### Reproduction

```tsx
import { MantineProvider, useMantineClassNamesPrefix } from '@mantine/core';

function TestComponent() {
  const prefix = useMantineClassNamesPrefix();
  console.log(prefix); // Returns undefined or falls back to 'prefix' property
  return <div>Check console</div>;
}

function App() {
  return (
    <MantineProvider classNamesPrefix="mantine">
      <TestComponent />
    </MantineProvider>
  );
}
```

### Expected behavior

The hook should return the `classNamesPrefix` value that was passed to `MantineProvider`. In the example above, it should return `"mantine"` but instead returns `undefined` or falls back to the wrong property.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
