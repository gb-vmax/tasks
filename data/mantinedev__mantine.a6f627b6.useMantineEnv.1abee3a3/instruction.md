# Bug Report

### Describe the bug

The `useMantineEnv()` hook is returning an empty object instead of the environment value. When trying to access the `env` property from the Mantine context, it's not working as expected.

### Reproduction

```tsx
import { useMantineEnv } from '@mantine/core';

function MyComponent() {
  const env = useMantineEnv();
  
  // Expected: 'default' or the configured env value
  // Actual: {} (empty object)
  console.log(env);
  
  return <div>Check console</div>;
}
```

### Expected behavior

`useMantineEnv()` should return the environment string value (e.g., 'default' or whatever is configured in the MantineProvider), not an empty object.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
