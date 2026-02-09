# Bug Report

### Describe the bug

The `useMantineContext` hook is not throwing an error when `MantineProvider` is missing from the component tree. Instead, it returns `undefined` silently, which can lead to confusing runtime errors later in the application when trying to access context properties.

### Reproduction

```jsx
import { useMantineContext } from '@mantine/core';

function MyComponent() {
  // This should throw an error but doesn't
  const ctx = useMantineContext();
  
  // Later trying to access ctx properties causes unexpected errors
  console.log(ctx.theme); // TypeError: Cannot read properties of undefined
  
  return <div>Component content</div>;
}

// Render MyComponent WITHOUT wrapping it in MantineProvider
<MyComponent />
```

### Expected behavior

When `useMantineContext` is called outside of a `MantineProvider`, it should immediately throw a clear error message: `[@mantine/core] MantineProvider was not found in tree`

This would help developers quickly identify that they forgot to wrap their app/component in `MantineProvider`.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
