# Bug Report

### Describe the bug

The `useIsBrowser()` hook is always returning `true` regardless of whether the code is running in a browser or during server-side rendering. This breaks the ability to conditionally render browser-only code and causes hydration mismatches.

### Reproduction

```jsx
import useIsBrowser from '@docusaurus/useIsBrowser';

function MyComponent() {
  const isBrowser = useIsBrowser();
  
  console.log('isBrowser:', isBrowser);
  // Always logs: isBrowser: true
  // Even during SSR, this returns true
  
  if (isBrowser) {
    // This code runs during SSR when it shouldn't
    return <div>{window.location.href}</div>;
  }
  
  return <div>Loading...</div>;
}
```

### Expected behavior

During server-side rendering, `useIsBrowser()` should return `false`. It should only return `true` when the code is actually running in the browser environment. This allows components to safely use browser-only APIs without causing SSR errors.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
