# Bug Report

### Describe the bug

The `useMantineIsHeadless()` hook is returning the opposite value of what it should. When the provider is configured with `headless: true`, the hook returns `false`, and when `headless: false`, it returns `true`.

### Reproduction

```jsx
import { MantineProvider, useMantineIsHeadless } from '@mantine/core';

function TestComponent() {
  const isHeadless = useMantineIsHeadless();
  console.log('isHeadless:', isHeadless); // Expected: true, Actual: false
  return <div>Check console</div>;
}

function App() {
  return (
    <MantineProvider headless={true}>
      <TestComponent />
    </MantineProvider>
  );
}
```

### Expected behavior

When `MantineProvider` is configured with `headless: true`, `useMantineIsHeadless()` should return `true`. When configured with `headless: false` or when the prop is omitted, it should return `false`.

Currently it's doing the exact opposite - returning `false` when headless mode is enabled and `true` when it's disabled.

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
