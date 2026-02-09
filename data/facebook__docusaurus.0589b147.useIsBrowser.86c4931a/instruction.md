# Bug Report

### Describe the bug

The `useIsBrowser()` hook is returning incorrect values in certain scenarios. It seems to be inverting the browser detection logic - returning `false` when code is running in the browser and `true` when running on the server.

### Reproduction

```jsx
import useIsBrowser from '@docusaurus/useIsBrowser';

function MyComponent() {
  const isBrowser = useIsBrowser();
  
  console.log('isBrowser:', isBrowser);
  // Expected: true (when running in browser)
  // Actual: false
  
  return (
    <div>
      {isBrowser ? 'Running in browser' : 'Running on server'}
    </div>
  );
}
```

When this component renders in the browser, it displays "Running on server" instead of "Running in browser".

### Expected behavior

`useIsBrowser()` should return `true` when the code is executing in a browser environment and `false` during SSR/build time.

### Additional context

This appears to have broken recently. Components that rely on this hook for conditional browser-only logic are now behaving incorrectly, trying to execute server-side code in the browser and vice versa.

---
Repository: /testbed
