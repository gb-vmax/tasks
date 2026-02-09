# Bug Report

### Describe the bug

The `useIsBrowser()` hook is returning inverted values - it returns `true` during SSR and `false` in the browser, which is the opposite of what it should do.

### Reproduction

```jsx
import useIsBrowser from '@docusaurus/useIsBrowser';

function MyComponent() {
  const isBrowser = useIsBrowser();
  
  console.log('isBrowser:', isBrowser);
  // During SSR: prints true (should be false)
  // In browser: prints false (should be true)
  
  return (
    <div>
      {isBrowser ? 'Running in browser' : 'Running on server'}
    </div>
  );
}
```

### Expected behavior

- `useIsBrowser()` should return `false` during server-side rendering
- `useIsBrowser()` should return `true` when running in the browser

Currently getting the opposite behavior - the hook returns `true` on the server and `false` in the browser.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
