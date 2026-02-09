# Bug Report

### Describe the bug

The `useMantineEnv()` hook is returning `undefined` instead of the expected environment value. After some investigation, it seems like the hook is not correctly accessing the environment property from the Mantine context.

### Reproduction

```tsx
import { useMantineEnv } from '@mantine/core';

function MyComponent() {
  const env = useMantineEnv();
  console.log(env); // Expected: 'default' or custom env value, Actual: undefined
  
  return <div>Environment: {env}</div>;
}
```

### Expected behavior

The `useMantineEnv()` hook should return the environment value from the context, or `'default'` as a fallback when no custom environment is set. Currently it's returning `undefined` which breaks components that depend on this value.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
