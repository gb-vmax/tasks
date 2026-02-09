# Bug Report

### Describe the bug

The `useRouteContext()` hook is throwing an error "Unexpected: no Docusaurus route context found" even when the context is properly provided. This makes it impossible to use the hook in components that are correctly wrapped with the Docusaurus context provider.

### Reproduction

```jsx
import useRouteContext from '@docusaurus/useRouteContext';

function MyComponent() {
  // This throws an error even though context exists
  const routeContext = useRouteContext();
  
  return <div>{routeContext.plugin}</div>;
}
```

The component is properly wrapped in the Docusaurus app structure, but calling `useRouteContext()` always throws the error about missing context.

### Expected behavior

When the Docusaurus route context is available, `useRouteContext()` should return the context object without throwing an error. The hook should only throw when the context is actually missing (i.e., when used outside of a Docusaurus route).

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
