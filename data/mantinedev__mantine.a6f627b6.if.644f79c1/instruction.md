# Bug Report

### Describe the bug

The `useMergedRef` hook is not properly assigning values to refs anymore. When I pass refs to components, they end up being `undefined` instead of containing the actual DOM element or value.

### Reproduction

```jsx
import { useRef } from 'react';
import { useMergedRef } from '@mantine/hooks';

function MyComponent() {
  const ref1 = useRef(null);
  const ref2 = useRef(null);
  const mergedRef = useMergedRef(ref1, ref2);

  useEffect(() => {
    console.log(ref1.current); // Expected: div element, Actual: undefined
    console.log(ref2.current); // Expected: div element, Actual: undefined
  }, []);

  return <div ref={mergedRef}>Hello</div>;
}
```

### Expected behavior

Both `ref1.current` and `ref2.current` should contain the div element after mounting. Instead, they remain `undefined`.

This also affects callback refs:

```jsx
const callbackRef = (node) => {
  console.log(node); // Expected: div element, Actual: undefined
};

const mergedRef = useMergedRef(callbackRef);
return <div ref={mergedRef}>Hello</div>;
```

The callback receives `undefined` instead of the actual node.

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
