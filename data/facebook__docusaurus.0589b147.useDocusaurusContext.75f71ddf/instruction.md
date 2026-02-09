# Bug Report

### Describe the bug

When using `useDocusaurusContext()` hook, the returned context object seems to be a new object on every render instead of maintaining reference equality. This is causing unnecessary re-renders in components that depend on the context.

### Reproduction

```jsx
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

function MyComponent() {
  const context = useDocusaurusContext();
  
  useEffect(() => {
    console.log('Context changed');
  }, [context]); // This fires on every render
  
  return <div>{context.siteConfig.title}</div>;
}
```

### Expected behavior

The context object should maintain the same reference across renders unless the actual context value changes. This would prevent unnecessary re-renders when using the context as a dependency in hooks like `useEffect`, `useMemo`, etc.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
