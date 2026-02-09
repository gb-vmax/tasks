# Bug Report

### Describe the bug

The `useRouteContext()` hook is throwing an error "Unexpected: no Docusaurus route context found" even when the context is properly set up and available. This is preventing components from accessing route context data.

### Reproduction

```jsx
import useRouteContext from '@docusaurus/useRouteContext';

function MyComponent() {
  // This throws an error even though context exists
  const routeContext = useRouteContext();
  
  return <div>{routeContext.plugin}</div>;
}
```

### Expected behavior

The hook should return the route context object when it's available. It should only throw an error when the context is actually missing (i.e., when the component is used outside of a Docusaurus route).

### Additional context

This seems to have broken recently. Components that were working fine before are now throwing errors when trying to access route context. The error occurs even when the component is properly nested within the Docusaurus app structure where the context provider should be present.

---
Repository: /testbed
