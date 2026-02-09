# Bug Report

### Describe the bug

The `useMediaQuery` hook is returning incorrect initial values when no `initialValue` is provided. It seems like the hook is now returning `true` by default instead of properly checking the media query match status during SSR/initial render.

### Reproduction

```jsx
import { useMediaQuery } from '@mantine/hooks';

function MyComponent() {
  // No initialValue provided
  const matches = useMediaQuery('(min-width: 768px)');
  
  console.log(matches); // Expected: false (if viewport < 768px)
                        // Actual: true (always returns true initially)
  
  return <div>{matches ? 'Desktop' : 'Mobile'}</div>;
}
```

### Expected behavior

When `initialValue` is not provided, the hook should:
1. Return `false` during SSR or when `window` is not available
2. Return the actual result of `window.matchMedia(query).matches` when available

Currently it's returning `true` in cases where it should return `false`, causing incorrect initial renders.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
