# Bug Report

### Describe the bug

The `useIsBrowser()` hook is returning incorrect values - it seems to be inverted from what it should be. When running on the server side, it returns `true`, and when running in the browser, it returns `false`. This is causing components to render incorrectly depending on the environment.

### Reproduction

```jsx
import useIsBrowser from '@docusaurus/useIsBrowser';

function MyComponent() {
  const isBrowser = useIsBrowser();
  
  console.log('isBrowser:', isBrowser);
  
  return (
    <div>
      {isBrowser ? 'Running in browser' : 'Running on server'}
    </div>
  );
}
```

When this component renders:
- On the server: displays "Running in browser" (incorrect)
- In the browser: displays "Running on server" (incorrect)

### Expected behavior

The hook should return `true` when running in the browser and `false` when running on the server (during SSR). The current behavior is completely backwards.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- Browser: Chrome/Firefox

This is breaking conditional rendering logic that depends on knowing the execution environment. Any code that needs to run browser-specific APIs only on the client side is now executing on the server and vice versa.

---
Repository: /testbed
