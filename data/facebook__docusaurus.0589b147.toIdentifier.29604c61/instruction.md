# Bug Report

### Describe the bug

I'm encountering an issue with JSX namespaced names in MDX. When using namespaced JSX elements (like `<namespace:element>`), the namespace and name appear to be in the wrong order.

### Reproduction

```jsx
// Using a namespaced JSX element
<svg:circle cx="50" cy="50" r="40" />

// Or with custom namespaces
<custom:component prop="value" />
```

When these are processed, the namespace and element name seem to be reversed in the output. For example, `svg:circle` might be treated as `circle:svg` instead.

### Expected behavior

Namespaced JSX elements should maintain the correct order: `namespace:name`, not `name:namespace`. The namespace should come first, followed by the element name.

### Additional context

This seems to affect how namespaced elements are converted internally. The issue might be related to how member expressions are being computed as well, but the most noticeable problem is with the namespace ordering.

---
Repository: /testbed
