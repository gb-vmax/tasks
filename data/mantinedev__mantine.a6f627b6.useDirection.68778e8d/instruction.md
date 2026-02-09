# Bug Report

### Describe the bug

After a recent update, the `useDirection` hook is returning an object with a `value` property instead of returning the direction context directly. This breaks existing code that was accessing the direction properties directly from the hook's return value.

### Reproduction

```tsx
import { useDirection } from '@mantine/core';

function MyComponent() {
  const direction = useDirection();
  
  // This used to work but now returns undefined
  console.log(direction.dir); // undefined
  console.log(direction.toggleDirection); // undefined
  
  // Now we have to access through .value which wasn't needed before
  console.log(direction.value.dir); // works but breaks existing code
}
```

### Expected behavior

The `useDirection` hook should return the direction context object directly with `dir` and `toggleDirection` properties, not wrapped in an object with a `value` property. This is how it worked previously and changing the return type breaks backward compatibility.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
