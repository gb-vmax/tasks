# Bug Report

### Describe the bug

JSX component names are not being recognized correctly. Components with capitalized names are being treated as native HTML elements instead of custom components.

### Reproduction

```jsx
function MyComponent() {
  return <div>Hello</div>;
}

function App() {
  return <MyComponent />; // This is incorrectly treated as a native element
}
```

When using JSX components with capitalized names (following React/JSX conventions), they're not being identified as component references. Instead, they're being treated as native HTML elements, which breaks the build.

### Expected behavior

Components with names starting with an uppercase letter should be recognized as component references, not native elements. This is standard JSX behavior where:
- `<div>` → native HTML element
- `<MyComponent>` → component reference

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
