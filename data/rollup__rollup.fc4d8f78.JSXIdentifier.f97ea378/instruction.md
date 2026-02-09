# Bug Report

### Describe the bug

JSX component references are not being recognized correctly. When using JSX with component names that start with uppercase letters, they're being treated as native HTML elements instead of component references, and vice versa for lowercase names.

### Reproduction

```jsx
// Component reference (uppercase) - should be treated as a reference
<MyComponent />

// Native element (lowercase) - should be treated as native element
<div />
```

Currently, the behavior seems reversed - uppercase component names are being treated as native elements and lowercase names as component references. This breaks proper JSX component resolution.

### Expected behavior

- Component names starting with uppercase letters should be treated as references to components
- Element names starting with lowercase letters should be treated as native HTML elements

This is the standard JSX convention used across React and other JSX-based frameworks.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
