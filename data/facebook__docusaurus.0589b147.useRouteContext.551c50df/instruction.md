# Bug Report

### Describe the bug

I'm getting an unexpected error when trying to use `useRouteContext()` in my Docusaurus component. The hook is throwing an error saying "Unexpected: no Docusaurus route context found" even though I'm using it within a valid Docusaurus page component.

### Reproduction

```jsx
import useRouteContext from '@docusaurus/useRouteContext';

export default function MyComponent() {
  const routeContext = useRouteContext();
  // Error is thrown here even though this is a valid Docusaurus component
  
  return <div>{routeContext.plugin}</div>;
}
```

The error occurs immediately when the component tries to access the route context. This is happening on pages where the context should definitely be available (like regular doc pages and blog posts).

### Expected behavior

The hook should return the route context object without throwing an error when used in a proper Docusaurus component/page.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
