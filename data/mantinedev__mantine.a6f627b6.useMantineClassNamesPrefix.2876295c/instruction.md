# Bug Report

### Describe the bug

The `useMantineClassNamesPrefix` hook is returning the entire context object instead of just the `classNamesPrefix` property. This breaks any component or code that expects to receive a string prefix value.

### Reproduction

```tsx
import { useMantineClassNamesPrefix } from '@mantine/core';

function MyComponent() {
  const prefix = useMantineClassNamesPrefix();
  
  // Expected: prefix is a string (e.g., 'mantine')
  // Actual: prefix is the entire context object
  
  console.log(typeof prefix); // prints 'object' instead of 'string'
  
  // This will fail because prefix is not a string
  const className = `${prefix}-button`;
  
  return <div className={className}>Hello</div>;
}
```

### Expected behavior

`useMantineClassNamesPrefix()` should return the `classNamesPrefix` string value from the context, not the entire context object.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
