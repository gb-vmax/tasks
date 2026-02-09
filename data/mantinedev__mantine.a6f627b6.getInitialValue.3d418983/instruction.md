# Bug Report

### Describe the bug

The `useMediaQuery` hook is returning inverted boolean values. When a media query should match (return `true`), it returns `false`, and vice versa.

### Reproduction

```js
import { useMediaQuery } from '@mantine/hooks';

function MyComponent() {
  // Should return true on screens wider than 768px, but returns false
  const isLargeScreen = useMediaQuery('(min-width: 768px)');
  
  console.log('Is large screen:', isLargeScreen);
  // Expected: true (on large screens)
  // Actual: false (on large screens)
  
  return <div>{isLargeScreen ? 'Large' : 'Small'}</div>;
}
```

### Expected behavior

The hook should return `true` when the media query matches and `false` when it doesn't match. Currently getting the opposite behavior.

### System Info
- @mantine/hooks version: latest
- Browser: Chrome/Firefox
- OS: macOS

---
Repository: /testbed
