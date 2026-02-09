# Bug Report

### Describe the bug

JSX component detection is not working correctly. Components with uppercase first letters are being treated as native HTML elements instead of custom components, and vice versa. This causes incorrect bundling and tree-shaking behavior.

### Reproduction

```jsx
// Custom component - should be treated as a reference
<MyComponent />  // Incorrectly treated as native element

// Native element - should be treated as native
<div />  // Works correctly

// Component starting with lowercase but ending with uppercase
<componentA />  // Incorrectly treated as a reference
```

When using JSX components, the bundler is not correctly identifying which identifiers are custom components versus native HTML elements. This leads to:
- Custom components not being properly imported
- Tree-shaking removing code that should be kept
- Runtime errors about undefined components

### Expected behavior

Components starting with an uppercase letter (e.g., `MyComponent`) should be identified as custom component references, while elements starting with lowercase letters (e.g., `div`, `span`) should be treated as native HTML elements.

### Additional context

This affects JSX member expressions as well - the wrong part of the expression is being checked for determining the identifier type.

---
Repository: /testbed
