# Bug Report

### Describe the bug

JSX component references are being incorrectly classified as native elements, and vice versa. Components that start with uppercase letters are being treated as native HTML elements, while lowercase elements are being treated as component references.

### Reproduction

```jsx
// This component reference is incorrectly treated as a native element
<MyComponent />

// This native element is incorrectly treated as a component reference
<div />
```

When bundling code with JSX, the component detection logic appears to be inverted. Custom components (starting with uppercase) should be treated as references, but they're being identified as native elements instead. Similarly, native HTML elements (lowercase) are being misidentified as component references.

### Expected behavior

- JSX elements starting with uppercase letters (e.g., `<MyComponent />`) should be treated as component references
- JSX elements starting with lowercase letters (e.g., `<div />`) should be treated as native HTML element names

### Additional context

This seems to affect how the bundler handles JSX transformation and could lead to incorrect output or runtime errors when components aren't properly resolved.

---
Repository: /testbed
