# Bug Report

### Describe the bug

The `useRouteContext()` hook is throwing an error "Unexpected: no Docusaurus route context found" even when used inside a valid Docusaurus page component. This makes it impossible to access route context data in components.

### Reproduction

```jsx
import useRouteContext from '@docusaurus/useRouteContext';

function MyComponent() {
  // This throws an error even though the component is rendered within Docusaurus
  const routeContext = useRouteContext();
  
  return <div>{routeContext.plugin}</div>;
}
```

When trying to use this component in a Docusaurus page, I get the error:
```
Error: Unexpected: no Docusaurus route context found
```

### Expected behavior

The hook should return the route context object containing plugin information and other route-related data when used within a Docusaurus page. It should only throw an error when used outside of the Docusaurus context provider.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
