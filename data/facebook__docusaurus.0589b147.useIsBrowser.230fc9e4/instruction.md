# Bug Report

### Describe the bug

The `useIsBrowser()` hook is returning incorrect values after component re-renders. On initial render it correctly identifies the browser environment, but subsequent re-renders cause it to return stale or unexpected values.

### Reproduction

```jsx
function MyComponent() {
  const isBrowser = useIsBrowser();
  const [count, setCount] = useState(0);
  
  console.log('isBrowser:', isBrowser);
  
  return (
    <div>
      <p>Is Browser: {isBrowser ? 'true' : 'false'}</p>
      <button onClick={() => setCount(count + 1)}>Re-render</button>
    </div>
  );
}
```

Steps to reproduce:
1. Create a component that uses `useIsBrowser()`
2. Trigger a re-render (e.g., by updating state)
3. The `useIsBrowser()` value may change unexpectedly between renders

### Expected behavior

`useIsBrowser()` should consistently return the same value across all renders within the same environment. If it's running in a browser, it should always return `true`. If it's running during SSR, it should always return `false`.

The hook should not change its return value based on component re-renders.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- React version: 18.x

---
Repository: /testbed
