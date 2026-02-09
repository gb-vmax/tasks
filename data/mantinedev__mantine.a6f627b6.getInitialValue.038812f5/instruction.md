# Bug Report

### Describe the bug

The `useMediaQuery` hook is returning `undefined` instead of the actual media query match result when no `initialValue` is provided. It seems like the hook is not properly detecting the media query state on initial render.

### Reproduction

```js
import { useMediaQuery } from '@mantine/hooks';

function MyComponent() {
  // Should return true/false based on screen size, but returns undefined
  const isMobile = useMediaQuery('(max-width: 768px)');
  
  console.log(isMobile); // logs: undefined (expected: true or false)
  
  return <div>{isMobile ? 'Mobile' : 'Desktop'}</div>;
}
```

### Expected behavior

When `initialValue` is not provided, the hook should check `window.matchMedia(query).matches` and return the actual boolean value based on whether the media query matches or not.

### System Info
- @mantine/hooks version: latest
- Browser: Chrome/Firefox
- Environment: Client-side rendering

---
Repository: /testbed
