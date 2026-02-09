# Bug Report

### Describe the bug

I'm experiencing an issue with `useMergedRef` where ref callbacks are being called twice with the same value. This causes side effects in the callback to execute multiple times unexpectedly.

### Reproduction

```jsx
import { useMergedRef } from '@mantine/hooks';

function MyComponent() {
  const refCallback = (node) => {
    console.log('Ref callback called:', node);
    // This gets logged twice with the same node
  };

  const mergedRef = useMergedRef(refCallback);

  return <div ref={mergedRef}>Content</div>;
}
```

### Expected behavior

The ref callback should only be called once when the element is mounted/updated. Currently it's being invoked twice, which breaks any side effects that should only happen once (like initializing third-party libraries, measuring elements, etc.).

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
