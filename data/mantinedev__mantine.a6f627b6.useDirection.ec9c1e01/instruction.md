# Bug Report

### Describe the bug

After a recent update, the `useDirection()` hook is returning an unexpected object structure. Previously it returned the direction context value directly, but now it's wrapped in an additional object with a `value` property.

### Reproduction

```tsx
import { useDirection } from '@mantine/core';

function MyComponent() {
  const direction = useDirection();
  
  // This used to work but now direction.dir is undefined
  console.log(direction.dir); // undefined
  
  // Now you have to access it like this
  console.log(direction.value.dir); // 'ltr' or 'rtl'
  
  return <div>Check console</div>;
}
```

### Expected behavior

The hook should return the direction context value directly without wrapping it in an extra object. Components that were accessing `direction.dir` or `direction.setDirection` directly are now broken because they need to access `direction.value.dir` instead.

This is breaking existing code that relies on the previous API.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
