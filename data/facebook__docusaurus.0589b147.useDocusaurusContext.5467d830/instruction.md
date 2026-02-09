# Bug Report

### Describe the bug

I'm experiencing an issue where `useDocusaurusContext()` returns stale context data when the context changes. After the initial call, subsequent calls to the hook return the same cached context even when the actual context has been updated.

### Reproduction

```jsx
function MyComponent() {
  const context1 = useDocusaurusContext();
  console.log(context1.siteConfig.title); // "Site A"
  
  // ... context provider updates with new values ...
  
  const context2 = useDocusaurusContext();
  console.log(context2.siteConfig.title); // Still "Site A", expected "Site B"
}
```

Steps to reproduce:
1. Call `useDocusaurusContext()` in a component
2. Update the context provider with new values
3. Call `useDocusaurusContext()` again in the same or different component
4. The hook returns the old cached context instead of the updated one

### Expected behavior

The hook should return the current context value from the React Context, not a cached value. Each call should respect React's context updates and re-render behavior.

### System Info

- Docusaurus version: latest
- Node version: 18.x
- React version: 18.x

---
Repository: /testbed
