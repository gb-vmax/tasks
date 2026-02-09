# Bug Report

### Describe the bug

The `useMantineEnv()` hook is returning incorrect values. Instead of returning the actual environment string (e.g., 'default', 'production', etc.), it's returning boolean `true` or `undefined`.

### Reproduction

```tsx
import { useMantineEnv } from '@mantine/core';

function MyComponent() {
  const env = useMantineEnv();
  
  console.log(env); // Expected: 'default' or environment string
                    // Actual: true or undefined
  
  // This breaks any logic that depends on the actual env value
  if (env === 'default') {
    // This condition never works now
  }
}
```

### Expected behavior

`useMantineEnv()` should return the actual environment string value from the Mantine context, or 'default' as a fallback when no environment is set.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
