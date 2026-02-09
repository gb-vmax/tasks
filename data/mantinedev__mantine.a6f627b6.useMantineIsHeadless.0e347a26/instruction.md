# Bug Report

### Describe the bug

The `useMantineIsHeadless()` hook is returning an object with a `value` property instead of returning the boolean value directly. This breaks existing code that expects a boolean return value.

### Reproduction

```tsx
import { useMantineIsHeadless } from '@mantine/core';

function MyComponent() {
  const isHeadless = useMantineIsHeadless();
  
  // This now fails because isHeadless is an object, not a boolean
  if (isHeadless) {
    return <div>Headless mode</div>;
  }
  
  return <div>Normal mode</div>;
}
```

### Expected behavior

The hook should return a boolean value directly, not wrapped in an object. Previously, you could use it directly in conditionals like:

```tsx
const isHeadless = useMantineIsHeadless();
if (isHeadless) { /* ... */ }
```

Now it seems to return `{ value: boolean }` which means you have to access `.value` property, but this breaks backward compatibility.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
