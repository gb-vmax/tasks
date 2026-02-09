# Bug Report

### Describe the bug

The `useMediaQuery` hook is not respecting the `initialValue` parameter when provided. Instead of using the provided initial value, it appears to be using `undefined` or falling back to the media query match result even when an explicit initial value is passed.

### Reproduction

```js
import { useMediaQuery } from '@mantine/hooks';

function MyComponent() {
  // Passing initialValue: false, but it's being ignored
  const matches = useMediaQuery('(min-width: 768px)', false);
  
  console.log(matches); // Expected: false, but getting undefined or the actual match result
  
  return <div>{matches ? 'Desktop' : 'Mobile'}</div>;
}
```

### Expected behavior

When `initialValue` is explicitly provided to `useMediaQuery`, it should be used as the initial state before the media query listener is attached. This is particularly important for SSR scenarios or when you want to control the initial render state.

For example:
```js
useMediaQuery('(min-width: 768px)', false) // Should initially return false
useMediaQuery('(min-width: 768px)', true)  // Should initially return true
```

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Environment: Browser

This seems to have broken recently. The hook used to properly use the initialValue parameter but now it's not working as expected.

---
Repository: /testbed
