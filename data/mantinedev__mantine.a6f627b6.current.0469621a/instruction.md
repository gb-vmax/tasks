# Bug Report

### Describe the bug

When using the `useMove` hook, I'm getting errors when the component unmounts or when the ref changes. It looks like the event listeners aren't being cleaned up properly, which is causing memory leaks and console errors in my application.

### Reproduction

```jsx
import { useMove } from '@mantine/hooks';

function MyComponent() {
  const { ref, active } = useMove(({ x, y }) => {
    console.log(x, y);
  });

  return (
    <div ref={ref} style={{ width: 200, height: 200, background: 'blue' }}>
      Drag me
    </div>
  );
}

// When this component unmounts or the ref changes, 
// event listeners are not properly removed
```

### Expected behavior

Event listeners should be properly removed when the component unmounts or when the ref changes to prevent memory leaks. The cleanup function should work correctly without throwing errors.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
