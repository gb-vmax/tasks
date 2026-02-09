# Bug Report

### Describe the bug

JSX component references are not being detected correctly. When using JSX with component names that start with uppercase letters (following React conventions), they are being treated as native HTML elements instead of component references.

### Reproduction

```jsx
import MyComponent from './MyComponent';

function App() {
  return (
    <div>
      <MyComponent />
    </div>
  );
}
```

In the example above, `MyComponent` should be recognized as a component reference since it starts with an uppercase letter, but it's being treated as a native element name instead.

### Expected behavior

- Component names starting with uppercase letters (e.g., `MyComponent`, `Button`, `Header`) should be identified as component references
- Native HTML elements (e.g., `div`, `span`, `button`) should be identified as native element names

This is breaking proper JSX compilation and module inclusion for components.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
