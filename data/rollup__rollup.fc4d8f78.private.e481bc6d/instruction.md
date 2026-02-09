# Bug Report

### Describe the bug

JSX component references are being incorrectly identified as native elements, and vice versa. When using JSX syntax, components that should be treated as custom components (starting with uppercase letters) are being treated as native HTML elements, and native elements (starting with lowercase) are being treated as component references.

### Reproduction

```jsx
// This custom component is incorrectly treated as a native element
<MyComponent />

// This native element is incorrectly treated as a component reference
<div />
```

Additionally, there seems to be an issue with JSX member expressions where the wrong part of the expression is being identified:

```jsx
// The property reference is not being handled correctly
<Namespace.Component />
```

### Expected behavior

- Component names starting with uppercase letters (e.g., `MyComponent`) should be identified as component references
- Element names starting with lowercase letters (e.g., `div`, `span`) should be identified as native HTML elements
- In JSX member expressions like `Namespace.Component`, the property part should be correctly identified

### System Info

This appears to affect JSX/TSX processing in the AST parsing layer.

---
Repository: /testbed
