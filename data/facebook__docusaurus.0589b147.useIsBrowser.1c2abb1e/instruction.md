# Bug Report

### Describe the bug

The `useIsBrowser()` hook is returning incorrect values after a recent update. It seems to be inverted - returning `false` when running in the browser and `true` during SSR.

### Reproduction

```jsx
import useIsBrowser from '@docusaurus/useIsBrowser';

function MyComponent() {
  const isBrowser = useIsBrowser();
  
  console.log('isBrowser:', isBrowser);
  // Expected: true (when in browser)
  // Actual: false
  
  return (
    <div>
      {isBrowser ? 'Running in browser' : 'Running on server'}
    </div>
  );
}
```

### Expected behavior

- During SSR: `useIsBrowser()` should return `false`
- In the browser: `useIsBrowser()` should return `true`

Currently it's doing the opposite - showing "Running on server" when the component is actually rendered in the browser.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- Browser: Chrome/Firefox

This is breaking conditional rendering logic that depends on detecting the browser environment.

---
Repository: /testbed
