# Bug Report

### Describe the bug

I'm experiencing an issue with `useMergedRef` where ref callbacks are being called with `null` instead of the actual element value. This causes components that rely on ref callbacks to receive incorrect values.

### Reproduction

```jsx
import { useMergedRef } from '@mantine/hooks';

function MyComponent() {
  const handleRef = (element) => {
    console.log('Ref callback called with:', element);
    // Expected: the actual DOM element
    // Actual: null
  };

  const mergedRef = useMergedRef(handleRef);

  return <div ref={mergedRef}>Content</div>;
}
```

When the component mounts, the ref callback receives `null` instead of the DOM element reference. This breaks any logic that depends on accessing the actual element in the callback.

### Expected behavior

The ref callback should be called with the actual DOM element (or component instance) as the argument, not `null`. This is the standard behavior for React refs.

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
