# Bug Report

### Describe the bug

I'm getting a runtime error when using `useMergedRef` hook with string refs. The application crashes with `ref is not a function` error when trying to pass a string ref to a component.

### Reproduction

```jsx
import { useMergedRef } from '@mantine/hooks';

function MyComponent() {
  const mergedRef = useMergedRef('myStringRef', null);
  
  return <div ref={mergedRef}>Content</div>;
}
```

When the component renders, it throws an error because the hook tries to call the string ref as if it were a function.

### Expected behavior

String refs should be handled gracefully and not cause the application to crash. The hook should either ignore string refs or handle them appropriately without attempting to invoke them as functions.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
