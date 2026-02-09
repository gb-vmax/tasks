# Bug Report

### Describe the bug

The `useMantineEnv()` hook is always returning `'default'` instead of the actual environment value from the context. This breaks environment-specific behavior in components that rely on this hook.

### Reproduction

```tsx
import { MantineProvider, useMantineEnv } from '@mantine/core';

function TestComponent() {
  const env = useMantineEnv();
  console.log(env); // Always logs 'default' even when env is set
  return <div>{env}</div>;
}

function App() {
  return (
    <MantineProvider env="production">
      <TestComponent />
    </MantineProvider>
  );
}
```

### Expected behavior

When a custom environment is passed to `MantineProvider`, `useMantineEnv()` should return that environment value (e.g., `'production'`), not always `'default'`.

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
