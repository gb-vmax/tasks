# Bug Report

### Describe the bug
The `useMediaQuery` hook is not properly cleaning up event listeners in certain browser environments. After unmounting a component that uses this hook, the media query listeners remain attached, leading to memory leaks and potential unexpected behavior.

### Reproduction
```jsx
import { useMediaQuery } from '@mantine/hooks';

function MyComponent() {
  const matches = useMediaQuery('(min-width: 768px)');
  return <div>{matches ? 'Desktop' : 'Mobile'}</div>;
}

// Mount and unmount the component multiple times
// The event listeners are not being removed correctly
```

Steps to reproduce:
1. Create a component that uses `useMediaQuery`
2. Mount the component
3. Unmount the component
4. Repeat several times
5. Check browser DevTools for memory leaks - you'll see listeners accumulating

### Expected behavior
When a component using `useMediaQuery` is unmounted, all associated event listeners should be properly removed. The cleanup function should use the same method to remove listeners that was used to add them.

### System Info
- @mantine/hooks version: latest
- Browser: Chrome 120 / Safari 17
- React version: 18.x

This seems to be happening because the cleanup function is trying to remove listeners using a different method than what was used to add them in the first place.

---
Repository: /testbed
