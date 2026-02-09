# Bug Report

### Describe the bug

The `useMediaQuery` hook seems to have a memory leak issue. After unmounting components that use this hook, the media query listeners are not being properly cleaned up. I noticed my app's memory usage keeps growing when repeatedly mounting/unmounting components with media queries.

### Reproduction

```jsx
import { useMediaQuery } from '@mantine/hooks';

function MyComponent() {
  const matches = useMediaQuery('(min-width: 768px)');
  return <div>{matches ? 'Desktop' : 'Mobile'}</div>;
}

// Mount and unmount this component multiple times
// Memory usage keeps increasing
```

### Steps to reproduce:
1. Create a component using `useMediaQuery`
2. Mount the component
3. Unmount the component
4. Repeat steps 2-3 multiple times
5. Check browser memory usage - it keeps growing

### Expected behavior

When a component using `useMediaQuery` unmounts, all event listeners should be removed and memory should be freed. The cleanup function should properly remove the listeners that were added.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
