# Bug Report

### Describe the bug

I'm getting an unexpected error when trying to use `useRouteContext()` in my Docusaurus component. The hook is throwing an error saying "Unexpected: no Docusaurus route context found" even though I'm using it inside a valid Docusaurus page component.

### Reproduction

```jsx
import useRouteContext from '@docusaurus/useRouteContext';

function MyComponent() {
  const routeContext = useRouteContext();
  
  return <div>{routeContext.plugin}</div>;
}
```

When this component renders, it throws the error immediately.

### Expected behavior

The hook should return the route context object without throwing an error when used inside a Docusaurus page. The context should be available for all components rendered within the Docusaurus app.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- Browser: Chrome

---
Repository: /testbed
