# Bug Report

### Describe the bug

I'm experiencing an issue with `useMergedRef` where refs aren't being assigned correctly in certain cases. It seems like when passing a ref object, the value isn't being set properly and the ref remains `null` or `undefined`.

### Reproduction

```tsx
import { useMergedRef } from '@mantine/hooks';
import { useRef } from 'react';

function MyComponent() {
  const ref1 = useRef(null);
  const ref2 = useRef(null);
  const mergedRef = useMergedRef(ref1, ref2);

  // After rendering, ref1.current and ref2.current are not set correctly
  
  return <div ref={mergedRef}>Content</div>;
}
```

### Expected behavior

Both `ref1.current` and `ref2.current` should point to the same DOM element after the component mounts. The merged ref should properly assign the value to all provided refs.

### System Info

- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
