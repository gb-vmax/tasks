# Bug Report

### Describe the bug

The `useMantineIsHeadless()` hook is returning inverted boolean values. When `headless` is set to `true` in the MantineProvider, the hook returns `false`, and vice versa.

### Reproduction

```tsx
import { MantineProvider } from '@mantine/core';
import { useMantineIsHeadless } from '@mantine/core';

function TestComponent() {
  const isHeadless = useMantineIsHeadless();
  console.log('isHeadless:', isHeadless); // Expected: true, Actual: false
  return null;
}

function App() {
  return (
    <MantineProvider headless={true}>
      <TestComponent />
    </MantineProvider>
  );
}
```

When `headless={true}` is passed to MantineProvider, `useMantineIsHeadless()` returns `false` instead of `true`.

### Expected behavior

`useMantineIsHeadless()` should return the same boolean value as what was passed to the `headless` prop in MantineProvider. If `headless={true}`, the hook should return `true`. If `headless={false}` or not provided, it should return `false`.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
