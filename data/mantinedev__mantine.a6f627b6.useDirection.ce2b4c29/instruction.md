# Bug Report

### Describe the bug

I'm experiencing an issue with the `useDirection()` hook after a recent update. The hook is now returning an object with a different structure than expected, which breaks existing code that relies on the original return value format.

Previously, `useDirection()` would return the direction context directly, but now it seems to be wrapped in an additional object with a `value` property in some cases, making the return type inconsistent.

### Reproduction

```tsx
import { useDirection } from '@mantine/core';

function MyComponent() {
  const direction = useDirection();
  
  // This used to work but now fails
  console.log(direction.dir); // Expected: 'ltr' or 'rtl'
  
  // Sometimes direction.dir is undefined
  // and the actual value is at direction.value.dir
}
```

### Expected behavior

The `useDirection()` hook should consistently return the direction context object with the same structure. Components should be able to access `direction.dir` and `direction.setDirection` directly without checking for nested `value` properties.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
