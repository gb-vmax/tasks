# Bug Report

### Describe the bug

JSX member expressions and namespaced names are being converted incorrectly, resulting in reversed property/object references. When using JSX components with dot notation (e.g., `<Foo.Bar>`) or namespaced elements (e.g., `<svg:circle>`), the identifiers are being swapped in the wrong order.

### Reproduction

```jsx
// Example 1: Member expression
<Theme.Provider>
  <Content />
</Theme.Provider>

// Example 2: Namespaced name
<svg:circle cx="50" cy="50" r="40" />
```

When these are processed, the member expression `Theme.Provider` gets its object and property reversed, and the namespaced name `svg:circle` has its namespace and name reversed.

### Expected behavior

- For `<Theme.Provider>`, the object should be `Theme` and the property should be `Provider`
- For `<svg:circle>`, the namespace should be `svg` and the name should be `circle`

The identifiers should maintain their correct positions and not be swapped during conversion.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
